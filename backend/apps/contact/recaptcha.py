"""
Google reCAPTCHA v3 verification utility.
"""
import logging
import requests
from django.conf import settings

logger = logging.getLogger(__name__)

RECAPTCHA_VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'


def verify_recaptcha(token: str, action: str = None, min_score: float = 0.5) -> dict:
    """
    Verify reCAPTCHA v3 token with Google.

    Args:
        token: The reCAPTCHA token from frontend
        action: Expected action name (optional, for extra validation)
        min_score: Minimum acceptable score (0.0 to 1.0, default 0.5)

    Returns:
        dict with keys:
            - success: bool - Whether verification passed
            - score: float - Risk score (1.0 = likely human, 0.0 = likely bot)
            - action: str - The action name
            - error: str - Error message if failed
    """
    secret_key = getattr(settings, 'RECAPTCHA_SECRET_KEY', None)

    # If no secret key configured, skip verification (development mode)
    if not secret_key:
        logger.warning("RECAPTCHA_SECRET_KEY not configured, skipping verification")
        return {
            'success': True,
            'score': 1.0,
            'action': action or 'unknown',
            'error': None,
            'skipped': True
        }

    if not token:
        return {
            'success': False,
            'score': 0.0,
            'action': None,
            'error': 'No reCAPTCHA token provided'
        }

    try:
        response = requests.post(
            RECAPTCHA_VERIFY_URL,
            data={
                'secret': secret_key,
                'response': token
            },
            timeout=10
        )
        result = response.json()

        logger.info(f"reCAPTCHA response: success={result.get('success')}, score={result.get('score')}")

        if not result.get('success'):
            error_codes = result.get('error-codes', [])
            return {
                'success': False,
                'score': 0.0,
                'action': result.get('action'),
                'error': f"Verification failed: {', '.join(error_codes)}"
            }

        score = result.get('score', 0.0)
        result_action = result.get('action', '')

        # Check score threshold
        if score < min_score:
            logger.warning(f"reCAPTCHA score too low: {score} < {min_score}")
            return {
                'success': False,
                'score': score,
                'action': result_action,
                'error': f'Score too low: {score}'
            }

        # Optionally check action matches
        if action and result_action != action:
            logger.warning(f"reCAPTCHA action mismatch: expected {action}, got {result_action}")
            return {
                'success': False,
                'score': score,
                'action': result_action,
                'error': f'Action mismatch: expected {action}'
            }

        return {
            'success': True,
            'score': score,
            'action': result_action,
            'error': None
        }

    except requests.RequestException as e:
        logger.error(f"reCAPTCHA verification request failed: {str(e)}")
        return {
            'success': False,
            'score': 0.0,
            'action': None,
            'error': f'Verification request failed: {str(e)}'
        }
    except Exception as e:
        logger.error(f"reCAPTCHA verification error: {str(e)}")
        return {
            'success': False,
            'score': 0.0,
            'action': None,
            'error': str(e)
        }
