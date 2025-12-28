'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useQuery } from '@tanstack/react-query';
import { motion, AnimatePresence } from 'framer-motion';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import Link from 'next/link';
import Image from 'next/image';
import {
  User,
  Mail,
  Phone,
  MapPin,
  Calendar,
  Plane,
  Settings,
  LogOut,
  Camera,
  Edit3,
  Save,
  X,
  Bell,
  Globe,
  Shield,
  CreditCard,
  Clock,
  ChevronRight,
  Loader2,
  AlertCircle,
  Lock,
} from 'lucide-react';
import toast from 'react-hot-toast';
import { useAuthStore } from '@/store/authStore';
import { bookingsApi } from '@/lib/api';
import { formatCurrency } from '@/lib/utils';

const profileSchema = z.object({
  first_name: z.string().min(2, 'الاسم الأول مطلوب'),
  last_name: z.string().min(2, 'اسم العائلة مطلوب'),
  email: z.string().email('البريد الإلكتروني غير صالح'),
  phone: z.string().optional(),
  country: z.string().optional(),
  date_of_birth: z.string().optional(),
  nationality: z.string().optional(),
  preferred_language: z.enum(['en', 'ar']).optional(),
  newsletter_subscribed: z.boolean().optional(),
});

type ProfileFormData = z.infer<typeof profileSchema>;

type TabType = 'profile' | 'bookings' | 'settings';

interface Booking {
  id: number;
  booking_reference: string;
  tour: {
    id: number;
    name: string;
    slug: string;
    featured_image: string | null;
  };
  departure_date: string;
  status: string;
  total_price: string;
  created_at: string;
}

export default function ProfilePage() {
  const router = useRouter();
  const { user, isAuthenticated, isLoading, updateProfile, logout } = useAuthStore();
  const [activeTab, setActiveTab] = useState<TabType>('profile');
  const [isEditing, setIsEditing] = useState(false);
  const [isSaving, setIsSaving] = useState(false);

  // Fetch bookings
  const { data: bookingsData, isLoading: bookingsLoading } = useQuery<{ results: Booking[] }>({
    queryKey: ['user-bookings'],
    queryFn: async () => {
      const response = await bookingsApi.getAll();
      return response.data;
    },
    enabled: isAuthenticated && activeTab === 'bookings',
  });

  const bookings = bookingsData?.results || [];

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isDirty },
  } = useForm<ProfileFormData>({
    resolver: zodResolver(profileSchema),
  });

  useEffect(() => {
    if (!isAuthenticated && !isLoading) {
      router.push('/auth/login');
    }
  }, [isAuthenticated, isLoading, router]);

  useEffect(() => {
    if (user) {
      reset({
        first_name: user.first_name || '',
        last_name: user.last_name || '',
        email: user.email || '',
        phone: user.phone || '',
        country: user.country || '',
        date_of_birth: user.date_of_birth || '',
        nationality: user.nationality || '',
        preferred_language: user.preferred_language || 'en',
        newsletter_subscribed: user.newsletter_subscribed || false,
      });
    }
  }, [user, reset]);

  const onSubmit = async (data: ProfileFormData) => {
    setIsSaving(true);
    try {
      await updateProfile(data);
      toast.success('تم تحديث الملف الشخصي بنجاح');
      setIsEditing(false);
    } catch (error) {
      toast.error('فشل تحديث الملف الشخصي');
    } finally {
      setIsSaving(false);
    }
  };

  const handleLogout = async () => {
    await logout();
    toast.success('تم تسجيل الخروج بنجاح');
    router.push('/');
  };

  const tabs = [
    { id: 'profile' as TabType, label: 'الملف الشخصي', icon: User },
    { id: 'bookings' as TabType, label: 'حجوزاتي', icon: Plane },
    { id: 'settings' as TabType, label: 'الإعدادات', icon: Settings },
  ];

  const getStatusLabel = (status: string) => {
    const labels: Record<string, { text: string; color: string }> = {
      pending: { text: 'قيد الانتظار', color: 'bg-yellow-100 text-yellow-700' },
      confirmed: { text: 'مؤكد', color: 'bg-green-100 text-green-700' },
      cancelled: { text: 'ملغي', color: 'bg-red-100 text-red-700' },
      completed: { text: 'مكتمل', color: 'bg-blue-100 text-blue-700' },
    };
    return labels[status] || { text: status, color: 'bg-gray-100 text-gray-700' };
  };

  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <Loader2 className="w-12 h-12 animate-spin text-primary-500 mx-auto mb-4" />
          <p className="text-gray-600">جاري التحميل...</p>
        </div>
      </div>
    );
  }

  if (!user) {
    return null;
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header Banner */}
      <div className="bg-gradient-to-r from-primary-600 via-primary-500 to-secondary-500 h-48 relative overflow-hidden">
        <div className="absolute inset-0 opacity-20">
          <div className="absolute top-0 right-0 w-96 h-96 bg-white rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
          <div className="absolute bottom-0 left-0 w-72 h-72 bg-white rounded-full blur-3xl translate-y-1/2 -translate-x-1/2"></div>
        </div>
      </div>

      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 -mt-24">
        <div className="grid lg:grid-cols-4 gap-6">
          {/* Sidebar */}
          <div className="lg:col-span-1">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="bg-white rounded-2xl shadow-lg overflow-hidden"
            >
              {/* Profile Card */}
              <div className="p-6 text-center border-b border-gray-100">
                <div className="relative inline-block mb-4">
                  <div className="w-24 h-24 rounded-full bg-gradient-to-br from-primary-400 to-primary-600 flex items-center justify-center text-white text-3xl font-bold">
                    {user.first_name?.[0]?.toUpperCase() || 'U'}
                    {user.last_name?.[0]?.toUpperCase() || ''}
                  </div>
                  <button className="absolute bottom-0 right-0 w-8 h-8 bg-white rounded-full shadow-lg flex items-center justify-center text-gray-600 hover:text-primary-500 transition-colors">
                    <Camera className="w-4 h-4" />
                  </button>
                </div>
                <h2 className="text-xl font-bold text-gray-900">
                  {user.first_name} {user.last_name}
                </h2>
                <p className="text-gray-500 text-sm">{user.email}</p>
                <div className="mt-3 flex items-center justify-center gap-2 text-sm text-gray-600">
                  <Clock className="w-4 h-4" />
                  <span>عضو منذ 2024</span>
                </div>
              </div>

              {/* Navigation */}
              <nav className="p-4">
                {tabs.map((tab) => (
                  <button
                    key={tab.id}
                    onClick={() => setActiveTab(tab.id)}
                    className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl mb-1 transition-all ${
                      activeTab === tab.id
                        ? 'bg-primary-50 text-primary-600'
                        : 'text-gray-600 hover:bg-gray-50'
                    }`}
                  >
                    <tab.icon className="w-5 h-5" />
                    <span className="font-medium">{tab.label}</span>
                    {activeTab === tab.id && (
                      <ChevronRight className="w-4 h-4 mr-auto" />
                    )}
                  </button>
                ))}

                <hr className="my-4" />

                <button
                  onClick={handleLogout}
                  className="w-full flex items-center gap-3 px-4 py-3 rounded-xl text-red-600 hover:bg-red-50 transition-all"
                >
                  <LogOut className="w-5 h-5" />
                  <span className="font-medium">تسجيل الخروج</span>
                </button>
              </nav>
            </motion.div>
          </div>

          {/* Main Content */}
          <div className="lg:col-span-3">
            <AnimatePresence mode="wait">
              {/* Profile Tab */}
              {activeTab === 'profile' && (
                <motion.div
                  key="profile"
                  initial={{ opacity: 0, x: 20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: -20 }}
                  className="bg-white rounded-2xl shadow-lg p-6"
                >
                  <div className="flex items-center justify-between mb-6">
                    <div>
                      <h3 className="text-xl font-bold text-gray-900">المعلومات الشخصية</h3>
                      <p className="text-gray-500 text-sm">قم بتحديث معلوماتك الشخصية</p>
                    </div>
                    {!isEditing ? (
                      <button
                        onClick={() => setIsEditing(true)}
                        className="flex items-center gap-2 px-4 py-2 bg-primary-50 text-primary-600 rounded-lg hover:bg-primary-100 transition-colors"
                      >
                        <Edit3 className="w-4 h-4" />
                        تعديل
                      </button>
                    ) : (
                      <button
                        onClick={() => {
                          setIsEditing(false);
                          reset();
                        }}
                        className="flex items-center gap-2 px-4 py-2 bg-gray-100 text-gray-600 rounded-lg hover:bg-gray-200 transition-colors"
                      >
                        <X className="w-4 h-4" />
                        إلغاء
                      </button>
                    )}
                  </div>

                  <form onSubmit={handleSubmit(onSubmit)}>
                    <div className="grid md:grid-cols-2 gap-6">
                      {/* First Name */}
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                          الاسم الأول
                        </label>
                        <div className="relative">
                          <User className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                          <input
                            type="text"
                            {...register('first_name')}
                            disabled={!isEditing}
                            className={`w-full pl-12 pr-4 py-3 rounded-xl border border-gray-200
                                      ${isEditing ? 'bg-white focus:ring-2 focus:ring-primary-500' : 'bg-gray-50'}
                                      transition-all`}
                          />
                        </div>
                        {errors.first_name && (
                          <p className="mt-1 text-sm text-red-500">{errors.first_name.message}</p>
                        )}
                      </div>

                      {/* Last Name */}
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                          اسم العائلة
                        </label>
                        <div className="relative">
                          <User className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                          <input
                            type="text"
                            {...register('last_name')}
                            disabled={!isEditing}
                            className={`w-full pl-12 pr-4 py-3 rounded-xl border border-gray-200
                                      ${isEditing ? 'bg-white focus:ring-2 focus:ring-primary-500' : 'bg-gray-50'}
                                      transition-all`}
                          />
                        </div>
                        {errors.last_name && (
                          <p className="mt-1 text-sm text-red-500">{errors.last_name.message}</p>
                        )}
                      </div>

                      {/* Email */}
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                          البريد الإلكتروني
                        </label>
                        <div className="relative">
                          <Mail className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                          <input
                            type="email"
                            {...register('email')}
                            disabled
                            className="w-full pl-12 pr-4 py-3 rounded-xl border border-gray-200 bg-gray-50"
                          />
                        </div>
                        <p className="mt-1 text-xs text-gray-500">البريد الإلكتروني لا يمكن تغييره</p>
                      </div>

                      {/* Phone */}
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                          رقم الهاتف
                        </label>
                        <div className="relative">
                          <Phone className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                          <input
                            type="tel"
                            {...register('phone')}
                            disabled={!isEditing}
                            className={`w-full pl-12 pr-4 py-3 rounded-xl border border-gray-200
                                      ${isEditing ? 'bg-white focus:ring-2 focus:ring-primary-500' : 'bg-gray-50'}
                                      transition-all`}
                            placeholder="+20 xxx xxx xxxx"
                          />
                        </div>
                      </div>

                      {/* Country */}
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                          الدولة
                        </label>
                        <div className="relative">
                          <MapPin className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                          <input
                            type="text"
                            {...register('country')}
                            disabled={!isEditing}
                            className={`w-full pl-12 pr-4 py-3 rounded-xl border border-gray-200
                                      ${isEditing ? 'bg-white focus:ring-2 focus:ring-primary-500' : 'bg-gray-50'}
                                      transition-all`}
                            placeholder="مصر"
                          />
                        </div>
                      </div>

                      {/* Date of Birth */}
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                          تاريخ الميلاد
                        </label>
                        <div className="relative">
                          <Calendar className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                          <input
                            type="date"
                            {...register('date_of_birth')}
                            disabled={!isEditing}
                            className={`w-full pl-12 pr-4 py-3 rounded-xl border border-gray-200
                                      ${isEditing ? 'bg-white focus:ring-2 focus:ring-primary-500' : 'bg-gray-50'}
                                      transition-all`}
                          />
                        </div>
                      </div>

                      {/* Nationality */}
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                          الجنسية
                        </label>
                        <div className="relative">
                          <Globe className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                          <input
                            type="text"
                            {...register('nationality')}
                            disabled={!isEditing}
                            className={`w-full pl-12 pr-4 py-3 rounded-xl border border-gray-200
                                      ${isEditing ? 'bg-white focus:ring-2 focus:ring-primary-500' : 'bg-gray-50'}
                                      transition-all`}
                            placeholder="مصري"
                          />
                        </div>
                      </div>

                      {/* Preferred Language */}
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                          اللغة المفضلة
                        </label>
                        <select
                          {...register('preferred_language')}
                          disabled={!isEditing}
                          className={`w-full px-4 py-3 rounded-xl border border-gray-200
                                    ${isEditing ? 'bg-white focus:ring-2 focus:ring-primary-500' : 'bg-gray-50'}
                                    transition-all`}
                        >
                          <option value="ar">العربية</option>
                          <option value="en">English</option>
                        </select>
                      </div>
                    </div>

                    {/* Newsletter */}
                    <div className="mt-6 p-4 bg-gray-50 rounded-xl">
                      <label className="flex items-center gap-3 cursor-pointer">
                        <input
                          type="checkbox"
                          {...register('newsletter_subscribed')}
                          disabled={!isEditing}
                          className="w-5 h-5 rounded border-gray-300 text-primary-500 focus:ring-primary-500"
                        />
                        <div>
                          <p className="font-medium text-gray-900">النشرة البريدية</p>
                          <p className="text-sm text-gray-500">
                            تلقي أحدث العروض والنصائح السياحية
                          </p>
                        </div>
                      </label>
                    </div>

                    {/* Save Button */}
                    {isEditing && (
                      <motion.div
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="mt-6 flex justify-end gap-3"
                      >
                        <button
                          type="submit"
                          disabled={isSaving || !isDirty}
                          className="flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-primary-500 to-primary-600 text-white rounded-xl font-semibold
                                   hover:from-primary-600 hover:to-primary-700 disabled:opacity-50 transition-all"
                        >
                          {isSaving ? (
                            <>
                              <Loader2 className="w-5 h-5 animate-spin" />
                              جاري الحفظ...
                            </>
                          ) : (
                            <>
                              <Save className="w-5 h-5" />
                              حفظ التغييرات
                            </>
                          )}
                        </button>
                      </motion.div>
                    )}
                  </form>
                </motion.div>
              )}

              {/* Bookings Tab */}
              {activeTab === 'bookings' && (
                <motion.div
                  key="bookings"
                  initial={{ opacity: 0, x: 20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: -20 }}
                  className="space-y-4"
                >
                  <div className="bg-white rounded-2xl shadow-lg p-6">
                    <h3 className="text-xl font-bold text-gray-900 mb-6">حجوزاتي</h3>

                    {bookingsLoading ? (
                      <div className="flex items-center justify-center py-12">
                        <Loader2 className="w-8 h-8 animate-spin text-primary-500" />
                        <span className="mr-3 text-gray-600">جاري تحميل الحجوزات...</span>
                      </div>
                    ) : bookings.length > 0 ? (
                      <div className="space-y-4">
                        {bookings.map((booking) => {
                          const statusInfo = getStatusLabel(booking.status);
                          return (
                            <Link
                              key={booking.id}
                              href={`/bookings/${booking.booking_reference}`}
                              className="flex items-center gap-4 p-4 bg-gray-50 rounded-xl hover:bg-gray-100 transition-colors"
                            >
                              <div className="w-20 h-20 rounded-xl overflow-hidden relative flex-shrink-0">
                                {booking.tour.featured_image ? (
                                  <Image
                                    src={booking.tour.featured_image}
                                    alt={booking.tour.name}
                                    fill
                                    className="object-cover"
                                  />
                                ) : (
                                  <div className="w-full h-full bg-gradient-to-br from-primary-400 to-primary-600 flex items-center justify-center text-white">
                                    <Plane className="w-8 h-8" />
                                  </div>
                                )}
                              </div>
                              <div className="flex-1 min-w-0">
                                <h4 className="font-semibold text-gray-900 truncate">{booking.tour.name}</h4>
                                <div className="flex items-center gap-4 mt-1 text-sm text-gray-500">
                                  <span className="flex items-center gap-1">
                                    <Calendar className="w-4 h-4" />
                                    {booking.departure_date}
                                  </span>
                                  <span
                                    className={`px-2 py-0.5 rounded-full text-xs font-medium ${statusInfo.color}`}
                                  >
                                    {statusInfo.text}
                                  </span>
                                </div>
                                <p className="text-xs text-gray-400 mt-1">
                                  رقم الحجز: {booking.booking_reference}
                                </p>
                              </div>
                              <div className="text-right">
                                <p className="text-lg font-bold text-primary-600">
                                  {formatCurrency(parseFloat(booking.total_price))}
                                </p>
                                <span className="text-sm text-primary-500">
                                  عرض التفاصيل
                                </span>
                              </div>
                            </Link>
                          );
                        })}
                      </div>
                    ) : (
                      <div className="text-center py-12">
                        <Plane className="w-16 h-16 text-gray-300 mx-auto mb-4" />
                        <h4 className="text-lg font-medium text-gray-900 mb-2">لا توجد حجوزات</h4>
                        <p className="text-gray-500 mb-4">ابدأ بحجز رحلتك الأولى الآن!</p>
                        <Link
                          href="/tours"
                          className="inline-block px-6 py-2 bg-primary-500 text-white rounded-lg hover:bg-primary-600 transition-colors"
                        >
                          استكشف الرحلات
                        </Link>
                      </div>
                    )}
                  </div>
                </motion.div>
              )}

              {/* Settings Tab */}
              {activeTab === 'settings' && (
                <motion.div
                  key="settings"
                  initial={{ opacity: 0, x: 20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: -20 }}
                  className="space-y-4"
                >
                  {/* Notifications */}
                  <div className="bg-white rounded-2xl shadow-lg p-6">
                    <div className="flex items-center gap-3 mb-6">
                      <div className="w-10 h-10 bg-primary-100 rounded-xl flex items-center justify-center">
                        <Bell className="w-5 h-5 text-primary-600" />
                      </div>
                      <div>
                        <h3 className="text-lg font-bold text-gray-900">الإشعارات</h3>
                        <p className="text-sm text-gray-500">إدارة تفضيلات الإشعارات</p>
                      </div>
                    </div>

                    <div className="space-y-4">
                      {[
                        { label: 'إشعارات البريد الإلكتروني', description: 'تلقي تحديثات الحجوزات' },
                        { label: 'إشعارات العروض', description: 'إشعارات بالعروض الجديدة والخصومات' },
                        { label: 'تذكيرات الرحلات', description: 'تذكير قبل موعد الرحلة' },
                      ].map((item, index) => (
                        <div key={index} className="flex items-center justify-between p-4 bg-gray-50 rounded-xl">
                          <div>
                            <p className="font-medium text-gray-900">{item.label}</p>
                            <p className="text-sm text-gray-500">{item.description}</p>
                          </div>
                          <label className="relative inline-flex items-center cursor-pointer">
                            <input type="checkbox" defaultChecked className="sr-only peer" />
                            <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary-500"></div>
                          </label>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Security */}
                  <div className="bg-white rounded-2xl shadow-lg p-6">
                    <div className="flex items-center gap-3 mb-6">
                      <div className="w-10 h-10 bg-green-100 rounded-xl flex items-center justify-center">
                        <Shield className="w-5 h-5 text-green-600" />
                      </div>
                      <div>
                        <h3 className="text-lg font-bold text-gray-900">الأمان</h3>
                        <p className="text-sm text-gray-500">إدارة إعدادات الأمان</p>
                      </div>
                    </div>

                    <div className="space-y-3">
                      <button className="w-full flex items-center justify-between p-4 bg-gray-50 rounded-xl hover:bg-gray-100 transition-colors">
                        <div className="flex items-center gap-3">
                          <Lock className="w-5 h-5 text-gray-500" />
                          <span className="font-medium text-gray-900">تغيير كلمة المرور</span>
                        </div>
                        <ChevronRight className="w-5 h-5 text-gray-400" />
                      </button>

                      <button className="w-full flex items-center justify-between p-4 bg-gray-50 rounded-xl hover:bg-gray-100 transition-colors">
                        <div className="flex items-center gap-3">
                          <CreditCard className="w-5 h-5 text-gray-500" />
                          <span className="font-medium text-gray-900">طرق الدفع</span>
                        </div>
                        <ChevronRight className="w-5 h-5 text-gray-400" />
                      </button>
                    </div>
                  </div>

                  {/* Danger Zone */}
                  <div className="bg-white rounded-2xl shadow-lg p-6 border border-red-100">
                    <div className="flex items-center gap-3 mb-4">
                      <div className="w-10 h-10 bg-red-100 rounded-xl flex items-center justify-center">
                        <AlertCircle className="w-5 h-5 text-red-600" />
                      </div>
                      <div>
                        <h3 className="text-lg font-bold text-gray-900">منطقة الخطر</h3>
                        <p className="text-sm text-gray-500">إجراءات لا يمكن التراجع عنها</p>
                      </div>
                    </div>

                    <button className="w-full py-3 border border-red-300 text-red-600 rounded-xl hover:bg-red-50 transition-colors font-medium">
                      حذف الحساب نهائياً
                    </button>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        </div>
      </div>
    </div>
  );
}
