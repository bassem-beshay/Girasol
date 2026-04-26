'use client';

import { useMemo } from 'react';
import DOMPurify from 'dompurify';

interface RichTextProps {
  html?: string | null;
  className?: string;
  as?: 'div' | 'span';
}

const ALLOWED_TAGS = [
  'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
  'p', 'br', 'hr',
  'ul', 'ol', 'li',
  'strong', 'em', 'b', 'i', 'u', 's',
  'a', 'img',
  'blockquote', 'pre', 'code',
  'table', 'thead', 'tbody', 'tr', 'th', 'td',
  'div', 'span',
  'figure', 'figcaption',
];

const ALLOWED_ATTR = [
  'href', 'src', 'alt', 'title', 'class', 'id',
  'target', 'rel', 'width', 'height', 'style',
];

export function RichText({ html, className, as = 'div' }: RichTextProps) {
  const clean = useMemo(() => {
    if (!html) return '';
    if (typeof window === 'undefined') return html;
    return DOMPurify.sanitize(html, {
      ALLOWED_TAGS,
      ALLOWED_ATTR,
      ALLOW_DATA_ATTR: false,
      ADD_ATTR: ['target'],
      FORBID_TAGS: ['script', 'iframe', 'form', 'input', 'button'],
      FORBID_ATTR: ['onerror', 'onload', 'onclick', 'onmouseover'],
    });
  }, [html]);

  if (!clean) return null;

  const Tag = as;
  return (
    <Tag
      className={`rich-text ${className ?? ''}`.trim()}
      dangerouslySetInnerHTML={{ __html: clean }}
    />
  );
}

export default RichText;
