import { MetadataRoute } from 'next';

const BASE_URL = 'https://girasoltours.com';
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

async function fetchSlugs(endpoint: string): Promise<string[]> {
  try {
    const res = await fetch(`${API_URL}/api${endpoint}`, {
      next: { revalidate: 86400 },
    });
    if (!res.ok) return [];
    const data = await res.json();
    const items = data.results || data;
    return Array.isArray(items) ? items.map((item: { slug: string }) => item.slug).filter(Boolean) : [];
  } catch {
    return [];
  }
}

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const [tourSlugs, destinationSlugs, blogSlugs] = await Promise.all([
    fetchSlugs('/tours/'),
    fetchSlugs('/destinations/'),
    fetchSlugs('/blog/posts/'),
  ]);

  const staticPages: MetadataRoute.Sitemap = [
    { url: BASE_URL, lastModified: new Date(), changeFrequency: 'daily', priority: 1.0 },
    { url: `${BASE_URL}/tours`, lastModified: new Date(), changeFrequency: 'daily', priority: 0.9 },
    { url: `${BASE_URL}/destinations`, lastModified: new Date(), changeFrequency: 'weekly', priority: 0.8 },
    { url: `${BASE_URL}/blog`, lastModified: new Date(), changeFrequency: 'weekly', priority: 0.7 },
    { url: `${BASE_URL}/contact`, lastModified: new Date(), changeFrequency: 'monthly', priority: 0.6 },
    { url: `${BASE_URL}/about/who-we-are`, lastModified: new Date(), changeFrequency: 'monthly', priority: 0.5 },
    { url: `${BASE_URL}/about/our-philosophy`, lastModified: new Date(), changeFrequency: 'monthly', priority: 0.5 },
    { url: `${BASE_URL}/about/service-quality`, lastModified: new Date(), changeFrequency: 'monthly', priority: 0.5 },
    { url: `${BASE_URL}/about/booking`, lastModified: new Date(), changeFrequency: 'monthly', priority: 0.5 },
    { url: `${BASE_URL}/terms`, lastModified: new Date(), changeFrequency: 'yearly', priority: 0.3 },
    { url: `${BASE_URL}/privacy`, lastModified: new Date(), changeFrequency: 'yearly', priority: 0.3 },
  ];

  const tourPages: MetadataRoute.Sitemap = tourSlugs.map((slug) => ({
    url: `${BASE_URL}/tours/${slug}`,
    lastModified: new Date(),
    changeFrequency: 'weekly',
    priority: 0.8,
  }));

  const destinationPages: MetadataRoute.Sitemap = destinationSlugs.map((slug) => ({
    url: `${BASE_URL}/destinations/${slug}`,
    lastModified: new Date(),
    changeFrequency: 'weekly',
    priority: 0.7,
  }));

  const blogPages: MetadataRoute.Sitemap = blogSlugs.map((slug) => ({
    url: `${BASE_URL}/blog/${slug}`,
    lastModified: new Date(),
    changeFrequency: 'weekly',
    priority: 0.6,
  }));

  return [...staticPages, ...tourPages, ...destinationPages, ...blogPages];
}
