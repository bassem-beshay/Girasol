"use client";

import Script from "next/script";

export default function RecaptchaScript() {
  return (
    <Script
      src={`https://www.google.com/recaptcha/api.js?render=${process.env.NEXT_PUBLIC_RECAPTCHA_SITE_KEY}`}
      strategy="afterInteractive"
      onLoad={() => {
        const setupBadge = () => {
          const badge = document.querySelector(".grecaptcha-badge") as HTMLElement | null;
          if (!badge) return false;

          // Force badge visible
          badge.style.setProperty("visibility", "visible", "important");
          badge.style.setProperty("opacity", "1", "important");

          // On mobile: tap badge to collapse it back
          badge.addEventListener("click", () => {
            // Temporarily disable hover effect by collapsing
            badge.style.setProperty("right", "-186px", "important");
            // Remove the override after a short delay so hover works again
            setTimeout(() => {
              badge.style.removeProperty("right");
            }, 300);
          });

          return true;
        };

        if (!setupBadge()) {
          const observer = new MutationObserver(() => {
            if (setupBadge()) observer.disconnect();
          });
          observer.observe(document.body, { childList: true, subtree: true });
          setTimeout(() => observer.disconnect(), 10000);
        }
      }}
    />
  );
}
