'use client';

import Image, { ImageProps } from 'next/image';
import { useState } from 'react';

interface ShimmerImageProps extends ImageProps {
  shimmerClassName?: string;
}

export function ShimmerImage({ shimmerClassName, className, onLoad, ...props }: ShimmerImageProps) {
  const [isLoaded, setIsLoaded] = useState(false);

  return (
    <div className={`relative ${shimmerClassName || ''}`}>
      {!isLoaded && (
        <div className="absolute inset-0 shimmer-loading rounded-inherit" />
      )}
      <Image
        {...props}
        className={`${className || ''} transition-opacity duration-500 ${isLoaded ? 'opacity-100' : 'opacity-0'}`}
        onLoad={(e) => {
          setIsLoaded(true);
          if (onLoad) onLoad(e);
        }}
      />
    </div>
  );
}
