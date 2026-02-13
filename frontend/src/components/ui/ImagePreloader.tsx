"use client";

import { useEffect, useRef } from "react";

/**
 * Preloads images before they enter the viewport.
 * Observes sections and loads their images when user is ~800px away.
 */
export function useImagePreloader() {
  const observerRef = useRef<IntersectionObserver | null>(null);

  useEffect(() => {
    if (typeof window === "undefined") return;

    // Find all lazy images and preload them when their container is near viewport
    const preloadNearbyImages = () => {
      const lazyImages = document.querySelectorAll('img[loading="lazy"]');

      observerRef.current = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              const img = entry.target as HTMLImageElement;
              // Force load by removing lazy and setting eager
              if (img.loading === "lazy") {
                img.loading = "eager";
                // Also preload srcset if exists
                if (img.srcset) {
                  const link = document.createElement("link");
                  link.rel = "preload";
                  link.as = "image";
                  link.imageSrcset = img.srcset;
                  link.imageSizes = img.sizes || "";
                  document.head.appendChild(link);
                } else if (img.src) {
                  const link = document.createElement("link");
                  link.rel = "preload";
                  link.as = "image";
                  link.href = img.src;
                  document.head.appendChild(link);
                }
              }
              observerRef.current?.unobserve(img);
            }
          });
        },
        {
          // Start loading when image is 800px below viewport
          rootMargin: "800px 0px",
          threshold: 0,
        }
      );

      lazyImages.forEach((img) => {
        observerRef.current?.observe(img);
      });
    };

    // Run after initial render
    const timer = setTimeout(preloadNearbyImages, 1000);

    // Re-run when new content loads (dynamic content)
    const mutationObserver = new MutationObserver(() => {
      const newLazyImages = document.querySelectorAll('img[loading="lazy"]');
      newLazyImages.forEach((img) => {
        observerRef.current?.observe(img);
      });
    });

    mutationObserver.observe(document.body, {
      childList: true,
      subtree: true,
    });

    return () => {
      clearTimeout(timer);
      observerRef.current?.disconnect();
      mutationObserver.disconnect();
    };
  }, []);
}
