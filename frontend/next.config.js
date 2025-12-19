/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'api.girasoltours.com',
        pathname: '/media/**',
      },
      {
        protocol: 'https',
        hostname: '*.s3.amazonaws.com',
        pathname: '/**',
      },
      {
        protocol: 'http',
        hostname: '50.6.250.81',
        pathname: '/media/**',
      },
      {
        protocol: 'http',
        hostname: 'localhost',
        pathname: '/media/**',
      },
    ],
  },
};

module.exports = nextConfig;
