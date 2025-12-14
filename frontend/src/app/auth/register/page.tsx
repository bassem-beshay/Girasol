'use client';

import { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { motion } from 'framer-motion';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import {
  Eye,
  EyeOff,
  Mail,
  Lock,
  User,
  ArrowRight,
  Loader2,
  Check,
  MapPin,
  Star,
  Heart,
} from 'lucide-react';
import toast from 'react-hot-toast';
import { useAuthStore } from '@/store/authStore';

const registerSchema = z
  .object({
    first_name: z.string().min(2, 'الاسم الأول يجب أن يكون حرفين على الأقل'),
    last_name: z.string().min(2, 'اسم العائلة يجب أن يكون حرفين على الأقل'),
    email: z.string().email('البريد الإلكتروني غير صالح'),
    password1: z
      .string()
      .min(8, 'كلمة المرور يجب أن تكون 8 أحرف على الأقل')
      .regex(/[A-Z]/, 'يجب أن تحتوي على حرف كبير واحد على الأقل')
      .regex(/[0-9]/, 'يجب أن تحتوي على رقم واحد على الأقل'),
    password2: z.string(),
    agreeToTerms: z.boolean().refine((val) => val === true, {
      message: 'يجب الموافقة على الشروط والأحكام',
    }),
    newsletter: z.boolean().optional(),
  })
  .refine((data) => data.password1 === data.password2, {
    message: 'كلمات المرور غير متطابقة',
    path: ['password2'],
  });

type RegisterFormData = z.infer<typeof registerSchema>;

export default function RegisterPage() {
  const router = useRouter();
  const { register: registerUser, isLoading, error, clearError } = useAuthStore();
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [currentStep, setCurrentStep] = useState(1);

  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<RegisterFormData>({
    resolver: zodResolver(registerSchema),
    defaultValues: {
      newsletter: true,
    },
  });

  const password = watch('password1', '');

  const passwordStrength = {
    length: password.length >= 8,
    uppercase: /[A-Z]/.test(password),
    number: /[0-9]/.test(password),
    special: /[!@#$%^&*]/.test(password),
  };

  const strengthScore = Object.values(passwordStrength).filter(Boolean).length;

  const onSubmit = async (data: RegisterFormData) => {
    try {
      await registerUser({
        email: data.email,
        password1: data.password1,
        password2: data.password2,
        first_name: data.first_name,
        last_name: data.last_name,
      });
      toast.success('تم إنشاء حسابك بنجاح! مرحباً بك');
      router.push('/profile');
    } catch (error) {
      // Error is handled in the store
    }
  };

  const testimonials = [
    {
      text: 'رحلة رائعة إلى الأقصر وأسوان! التنظيم كان ممتازاً',
      author: 'أحمد محمد',
      location: 'السعودية',
      rating: 5,
    },
    {
      text: 'أفضل تجربة سياحية في مصر. شكراً Girasol Tours!',
      author: 'سارة أحمد',
      location: 'الإمارات',
      rating: 5,
    },
  ];

  return (
    <div className="min-h-screen flex">
      {/* Left Side - Image & Testimonials */}
      <div className="hidden lg:flex lg:flex-1 relative bg-gradient-to-br from-secondary-600 via-secondary-500 to-primary-500">
        {/* Background Pattern */}
        <div className="absolute inset-0 opacity-10">
          <div className="absolute top-20 right-20 w-72 h-72 bg-white rounded-full blur-3xl"></div>
          <div className="absolute bottom-20 left-20 w-96 h-96 bg-white rounded-full blur-3xl"></div>
        </div>

        {/* Content */}
        <div className="relative z-10 flex flex-col justify-center p-16 text-white">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
          >
            <h2 className="text-4xl font-display font-bold mb-6">
              انضم إلى عائلة المسافرين
            </h2>
            <p className="text-xl text-white/80 mb-12 leading-relaxed">
              سجل الآن واحصل على عروض حصرية وتجارب سفر مميزة
            </p>

            {/* Benefits */}
            <div className="space-y-4 mb-12">
              {[
                { icon: MapPin, text: 'رحلات مخصصة حسب اهتماماتك' },
                { icon: Star, text: 'خصومات حصرية للأعضاء' },
                { icon: Heart, text: 'حفظ الرحلات المفضلة' },
              ].map((item, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ duration: 0.5, delay: 0.3 + index * 0.1 }}
                  className="flex items-center gap-4"
                >
                  <div className="w-10 h-10 rounded-lg bg-white/20 backdrop-blur-sm flex items-center justify-center">
                    <item.icon className="w-5 h-5" />
                  </div>
                  <span className="text-lg">{item.text}</span>
                </motion.div>
              ))}
            </div>

            {/* Testimonials */}
            <div className="space-y-4">
              {testimonials.map((testimonial, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5, delay: 0.6 + index * 0.1 }}
                  className="bg-white/10 backdrop-blur-sm rounded-2xl p-5"
                >
                  <div className="flex gap-1 mb-2">
                    {[...Array(testimonial.rating)].map((_, i) => (
                      <Star key={i} className="w-4 h-4 fill-yellow-400 text-yellow-400" />
                    ))}
                  </div>
                  <p className="text-white/90 mb-3">"{testimonial.text}"</p>
                  <div className="flex items-center gap-2 text-sm text-white/70">
                    <span className="font-medium text-white">{testimonial.author}</span>
                    <span>•</span>
                    <span>{testimonial.location}</span>
                  </div>
                </motion.div>
              ))}
            </div>
          </motion.div>
        </div>
      </div>

      {/* Right Side - Form */}
      <div className="flex-1 flex items-center justify-center p-8 bg-white overflow-y-auto">
        <motion.div
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.5 }}
          className="w-full max-w-md"
        >
          {/* Logo */}
          <Link href="/" className="inline-flex items-center gap-2 mb-8">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-primary-500 to-primary-600 flex items-center justify-center">
              <span className="text-white font-bold text-xl">G</span>
            </div>
            <span className="text-2xl font-display font-bold text-gray-900">
              Girasol Tours
            </span>
          </Link>

          {/* Header */}
          <div className="mb-8">
            <h1 className="text-3xl font-display font-bold text-gray-900 mb-2">
              إنشاء حساب جديد ✨
            </h1>
            <p className="text-gray-600">
              انضم إلينا واكتشف عالم من الرحلات المميزة
            </p>
          </div>

          {/* Progress Steps */}
          <div className="flex items-center gap-2 mb-8">
            {[1, 2].map((step) => (
              <div key={step} className="flex items-center gap-2">
                <div
                  className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium transition-colors ${
                    currentStep >= step
                      ? 'bg-primary-500 text-white'
                      : 'bg-gray-100 text-gray-400'
                  }`}
                >
                  {currentStep > step ? <Check className="w-4 h-4" /> : step}
                </div>
                {step < 2 && (
                  <div
                    className={`w-16 h-1 rounded-full transition-colors ${
                      currentStep > step ? 'bg-primary-500' : 'bg-gray-100'
                    }`}
                  />
                )}
              </div>
            ))}
          </div>

          {/* Error Alert */}
          {error && (
            <motion.div
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              className="mb-6 p-4 bg-red-50 border border-red-200 rounded-xl text-red-700 text-sm"
            >
              {error}
              <button
                onClick={clearError}
                className="float-right text-red-500 hover:text-red-700"
              >
                ✕
              </button>
            </motion.div>
          )}

          {/* Form */}
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-5">
            {currentStep === 1 && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="space-y-5"
              >
                {/* Name Fields */}
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      الاسم الأول
                    </label>
                    <div className="relative">
                      <User className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                      <input
                        type="text"
                        {...register('first_name')}
                        className={`w-full pl-12 pr-4 py-3.5 rounded-xl border ${
                          errors.first_name
                            ? 'border-red-300'
                            : 'border-gray-200'
                        } focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all bg-gray-50 focus:bg-white`}
                        placeholder="أحمد"
                      />
                    </div>
                    {errors.first_name && (
                      <p className="mt-1.5 text-sm text-red-500">
                        {errors.first_name.message}
                      </p>
                    )}
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      اسم العائلة
                    </label>
                    <div className="relative">
                      <User className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                      <input
                        type="text"
                        {...register('last_name')}
                        className={`w-full pl-12 pr-4 py-3.5 rounded-xl border ${
                          errors.last_name
                            ? 'border-red-300'
                            : 'border-gray-200'
                        } focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all bg-gray-50 focus:bg-white`}
                        placeholder="محمد"
                      />
                    </div>
                    {errors.last_name && (
                      <p className="mt-1.5 text-sm text-red-500">
                        {errors.last_name.message}
                      </p>
                    )}
                  </div>
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
                      className={`w-full pl-12 pr-4 py-3.5 rounded-xl border ${
                        errors.email ? 'border-red-300' : 'border-gray-200'
                      } focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all bg-gray-50 focus:bg-white`}
                      placeholder="example@email.com"
                    />
                  </div>
                  {errors.email && (
                    <p className="mt-1.5 text-sm text-red-500">{errors.email.message}</p>
                  )}
                </div>

                {/* Continue Button */}
                <button
                  type="button"
                  onClick={() => setCurrentStep(2)}
                  className="w-full py-3.5 px-6 bg-gradient-to-r from-primary-500 to-primary-600 text-white rounded-xl font-semibold
                           hover:from-primary-600 hover:to-primary-700 focus:ring-4 focus:ring-primary-500/30
                           transition-all duration-300 flex items-center justify-center gap-2"
                >
                  متابعة
                  <ArrowRight className="w-5 h-5" />
                </button>
              </motion.div>
            )}

            {currentStep === 2 && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="space-y-5"
              >
                {/* Password */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    كلمة المرور
                  </label>
                  <div className="relative">
                    <Lock className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                    <input
                      type={showPassword ? 'text' : 'password'}
                      {...register('password1')}
                      className={`w-full pl-12 pr-12 py-3.5 rounded-xl border ${
                        errors.password1 ? 'border-red-300' : 'border-gray-200'
                      } focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all bg-gray-50 focus:bg-white`}
                      placeholder="••••••••"
                    />
                    <button
                      type="button"
                      onClick={() => setShowPassword(!showPassword)}
                      className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"
                    >
                      {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                    </button>
                  </div>

                  {/* Password Strength Indicator */}
                  <div className="mt-3 space-y-2">
                    <div className="flex gap-1">
                      {[1, 2, 3, 4].map((level) => (
                        <div
                          key={level}
                          className={`h-1.5 flex-1 rounded-full transition-colors ${
                            strengthScore >= level
                              ? level <= 1
                                ? 'bg-red-500'
                                : level <= 2
                                ? 'bg-yellow-500'
                                : level <= 3
                                ? 'bg-blue-500'
                                : 'bg-green-500'
                              : 'bg-gray-200'
                          }`}
                        />
                      ))}
                    </div>
                    <div className="grid grid-cols-2 gap-2 text-xs">
                      <div className={`flex items-center gap-1 ${passwordStrength.length ? 'text-green-600' : 'text-gray-400'}`}>
                        <Check className="w-3 h-3" /> 8 أحرف على الأقل
                      </div>
                      <div className={`flex items-center gap-1 ${passwordStrength.uppercase ? 'text-green-600' : 'text-gray-400'}`}>
                        <Check className="w-3 h-3" /> حرف كبير
                      </div>
                      <div className={`flex items-center gap-1 ${passwordStrength.number ? 'text-green-600' : 'text-gray-400'}`}>
                        <Check className="w-3 h-3" /> رقم
                      </div>
                      <div className={`flex items-center gap-1 ${passwordStrength.special ? 'text-green-600' : 'text-gray-400'}`}>
                        <Check className="w-3 h-3" /> رمز خاص (اختياري)
                      </div>
                    </div>
                  </div>
                </div>

                {/* Confirm Password */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    تأكيد كلمة المرور
                  </label>
                  <div className="relative">
                    <Lock className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                    <input
                      type={showConfirmPassword ? 'text' : 'password'}
                      {...register('password2')}
                      className={`w-full pl-12 pr-12 py-3.5 rounded-xl border ${
                        errors.password2 ? 'border-red-300' : 'border-gray-200'
                      } focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all bg-gray-50 focus:bg-white`}
                      placeholder="••••••••"
                    />
                    <button
                      type="button"
                      onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                      className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"
                    >
                      {showConfirmPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                    </button>
                  </div>
                  {errors.password2 && (
                    <p className="mt-1.5 text-sm text-red-500">{errors.password2.message}</p>
                  )}
                </div>

                {/* Terms & Newsletter */}
                <div className="space-y-3">
                  <label className="flex items-start gap-3 cursor-pointer">
                    <input
                      type="checkbox"
                      {...register('agreeToTerms')}
                      className="w-5 h-5 rounded border-gray-300 text-primary-500 focus:ring-primary-500 mt-0.5"
                    />
                    <span className="text-sm text-gray-600">
                      أوافق على{' '}
                      <Link href="/terms" className="text-primary-600 hover:underline">
                        الشروط والأحكام
                      </Link>{' '}
                      و{' '}
                      <Link href="/privacy" className="text-primary-600 hover:underline">
                        سياسة الخصوصية
                      </Link>
                    </span>
                  </label>
                  {errors.agreeToTerms && (
                    <p className="text-sm text-red-500">{errors.agreeToTerms.message}</p>
                  )}

                  <label className="flex items-center gap-3 cursor-pointer">
                    <input
                      type="checkbox"
                      {...register('newsletter')}
                      className="w-5 h-5 rounded border-gray-300 text-primary-500 focus:ring-primary-500"
                    />
                    <span className="text-sm text-gray-600">
                      أريد تلقي العروض الحصرية والنصائح السياحية
                    </span>
                  </label>
                </div>

                {/* Buttons */}
                <div className="flex gap-3">
                  <button
                    type="button"
                    onClick={() => setCurrentStep(1)}
                    className="py-3.5 px-6 border border-gray-200 text-gray-700 rounded-xl font-semibold
                             hover:bg-gray-50 transition-all"
                  >
                    رجوع
                  </button>
                  <button
                    type="submit"
                    disabled={isLoading}
                    className="flex-1 py-3.5 px-6 bg-gradient-to-r from-primary-500 to-primary-600 text-white rounded-xl font-semibold
                             hover:from-primary-600 hover:to-primary-700 focus:ring-4 focus:ring-primary-500/30
                             transition-all duration-300 flex items-center justify-center gap-2 disabled:opacity-70"
                  >
                    {isLoading ? (
                      <>
                        <Loader2 className="w-5 h-5 animate-spin" />
                        جاري إنشاء الحساب...
                      </>
                    ) : (
                      <>
                        إنشاء الحساب
                        <ArrowRight className="w-5 h-5" />
                      </>
                    )}
                  </button>
                </div>
              </motion.div>
            )}
          </form>

          {/* Login Link */}
          <p className="mt-8 text-center text-gray-600">
            لديك حساب بالفعل؟{' '}
            <Link
              href="/auth/login"
              className="text-primary-600 hover:text-primary-700 font-semibold"
            >
              سجل دخولك
            </Link>
          </p>
        </motion.div>
      </div>
    </div>
  );
}
