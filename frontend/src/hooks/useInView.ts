'use client';

import { useState, useEffect, useRef, useCallback, RefCallback } from 'react';

interface UseInViewOptions {
  threshold?: number;
  rootMargin?: string;
  triggerOnce?: boolean;
}

export function useInView<T extends HTMLElement = HTMLDivElement>(
  options: UseInViewOptions = {}
): [RefCallback<T>, boolean] {
  const { threshold = 0, rootMargin = '100px', triggerOnce = true } = options;
  const [isInView, setIsInView] = useState(false);
  const observerRef = useRef<IntersectionObserver | null>(null);
  const elementRef = useRef<T | null>(null);

  const ref = useCallback((node: T | null) => {
    // Cleanup previous observer
    if (observerRef.current) {
      observerRef.current.disconnect();
    }

    if (!node) {
      elementRef.current = null;
      return;
    }

    elementRef.current = node;

    // Don't observe if already triggered and triggerOnce is true
    if (isInView && triggerOnce) return;

    observerRef.current = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsInView(true);
          if (triggerOnce && observerRef.current) {
            observerRef.current.disconnect();
          }
        } else if (!triggerOnce) {
          setIsInView(false);
        }
      },
      { threshold, rootMargin }
    );

    observerRef.current.observe(node);
  }, [threshold, rootMargin, triggerOnce, isInView]);

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      if (observerRef.current) {
        observerRef.current.disconnect();
      }
    };
  }, []);

  return [ref, isInView];
}
