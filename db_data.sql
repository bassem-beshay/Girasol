--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5
-- Dumped by pg_dump version 17.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: users_user; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: account_emailaddress; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: account_emailconfirmation; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_content_type VALUES (1, 'admin', 'logentry');
INSERT INTO public.django_content_type VALUES (2, 'auth', 'permission');
INSERT INTO public.django_content_type VALUES (3, 'auth', 'group');
INSERT INTO public.django_content_type VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO public.django_content_type VALUES (5, 'sessions', 'session');
INSERT INTO public.django_content_type VALUES (6, 'sites', 'site');
INSERT INTO public.django_content_type VALUES (7, 'authtoken', 'token');
INSERT INTO public.django_content_type VALUES (8, 'authtoken', 'tokenproxy');
INSERT INTO public.django_content_type VALUES (9, 'token_blacklist', 'blacklistedtoken');
INSERT INTO public.django_content_type VALUES (10, 'token_blacklist', 'outstandingtoken');
INSERT INTO public.django_content_type VALUES (11, 'account', 'emailaddress');
INSERT INTO public.django_content_type VALUES (12, 'account', 'emailconfirmation');
INSERT INTO public.django_content_type VALUES (13, 'socialaccount', 'socialaccount');
INSERT INTO public.django_content_type VALUES (14, 'socialaccount', 'socialapp');
INSERT INTO public.django_content_type VALUES (15, 'socialaccount', 'socialtoken');
INSERT INTO public.django_content_type VALUES (16, 'users', 'user');
INSERT INTO public.django_content_type VALUES (17, 'users', 'userprofile');
INSERT INTO public.django_content_type VALUES (18, 'users', 'wishlist');
INSERT INTO public.django_content_type VALUES (19, 'tours', 'tourcategory');
INSERT INTO public.django_content_type VALUES (20, 'tours', 'tour');
INSERT INTO public.django_content_type VALUES (21, 'tours', 'addon');
INSERT INTO public.django_content_type VALUES (22, 'tours', 'tourdeparture');
INSERT INTO public.django_content_type VALUES (23, 'tours', 'tourfaq');
INSERT INTO public.django_content_type VALUES (24, 'tours', 'tourhighlight');
INSERT INTO public.django_content_type VALUES (25, 'tours', 'tourimage');
INSERT INTO public.django_content_type VALUES (26, 'tours', 'tourinclusion');
INSERT INTO public.django_content_type VALUES (27, 'tours', 'touritinerary');
INSERT INTO public.django_content_type VALUES (28, 'tours', 'tourpricing');
INSERT INTO public.django_content_type VALUES (29, 'destinations', 'destination');
INSERT INTO public.django_content_type VALUES (30, 'destinations', 'area');
INSERT INTO public.django_content_type VALUES (31, 'destinations', 'activity');
INSERT INTO public.django_content_type VALUES (32, 'destinations', 'destinationimage');
INSERT INTO public.django_content_type VALUES (33, 'bookings', 'bookingaddon');
INSERT INTO public.django_content_type VALUES (34, 'bookings', 'payment');
INSERT INTO public.django_content_type VALUES (35, 'bookings', 'promocode');
INSERT INTO public.django_content_type VALUES (36, 'bookings', 'traveler');
INSERT INTO public.django_content_type VALUES (37, 'bookings', 'booking');
INSERT INTO public.django_content_type VALUES (38, 'blog', 'category');
INSERT INTO public.django_content_type VALUES (39, 'blog', 'post');
INSERT INTO public.django_content_type VALUES (40, 'blog', 'tag');
INSERT INTO public.django_content_type VALUES (41, 'blog', 'comment');
INSERT INTO public.django_content_type VALUES (42, 'reviews', 'reviewimage');
INSERT INTO public.django_content_type VALUES (43, 'reviews', 'testimonial');
INSERT INTO public.django_content_type VALUES (44, 'reviews', 'review');
INSERT INTO public.django_content_type VALUES (45, 'contact', 'faq');
INSERT INTO public.django_content_type VALUES (46, 'contact', 'inquiry');
INSERT INTO public.django_content_type VALUES (47, 'contact', 'inquiryresponse');
INSERT INTO public.django_content_type VALUES (48, 'contact', 'newsletter');
INSERT INTO public.django_content_type VALUES (49, 'contact', 'office');


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_permission VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO public.auth_permission VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO public.auth_permission VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO public.auth_permission VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO public.auth_permission VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO public.auth_permission VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO public.auth_permission VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO public.auth_permission VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO public.auth_permission VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO public.auth_permission VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO public.auth_permission VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO public.auth_permission VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO public.auth_permission VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO public.auth_permission VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO public.auth_permission VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO public.auth_permission VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO public.auth_permission VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO public.auth_permission VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO public.auth_permission VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO public.auth_permission VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO public.auth_permission VALUES (21, 'Can add site', 6, 'add_site');
INSERT INTO public.auth_permission VALUES (22, 'Can change site', 6, 'change_site');
INSERT INTO public.auth_permission VALUES (23, 'Can delete site', 6, 'delete_site');
INSERT INTO public.auth_permission VALUES (24, 'Can view site', 6, 'view_site');
INSERT INTO public.auth_permission VALUES (25, 'Can add Token', 7, 'add_token');
INSERT INTO public.auth_permission VALUES (26, 'Can change Token', 7, 'change_token');
INSERT INTO public.auth_permission VALUES (27, 'Can delete Token', 7, 'delete_token');
INSERT INTO public.auth_permission VALUES (28, 'Can view Token', 7, 'view_token');
INSERT INTO public.auth_permission VALUES (29, 'Can add token', 8, 'add_tokenproxy');
INSERT INTO public.auth_permission VALUES (30, 'Can change token', 8, 'change_tokenproxy');
INSERT INTO public.auth_permission VALUES (31, 'Can delete token', 8, 'delete_tokenproxy');
INSERT INTO public.auth_permission VALUES (32, 'Can view token', 8, 'view_tokenproxy');
INSERT INTO public.auth_permission VALUES (33, 'Can add blacklisted token', 9, 'add_blacklistedtoken');
INSERT INTO public.auth_permission VALUES (34, 'Can change blacklisted token', 9, 'change_blacklistedtoken');
INSERT INTO public.auth_permission VALUES (35, 'Can delete blacklisted token', 9, 'delete_blacklistedtoken');
INSERT INTO public.auth_permission VALUES (36, 'Can view blacklisted token', 9, 'view_blacklistedtoken');
INSERT INTO public.auth_permission VALUES (37, 'Can add outstanding token', 10, 'add_outstandingtoken');
INSERT INTO public.auth_permission VALUES (38, 'Can change outstanding token', 10, 'change_outstandingtoken');
INSERT INTO public.auth_permission VALUES (39, 'Can delete outstanding token', 10, 'delete_outstandingtoken');
INSERT INTO public.auth_permission VALUES (40, 'Can view outstanding token', 10, 'view_outstandingtoken');
INSERT INTO public.auth_permission VALUES (41, 'Can add email address', 11, 'add_emailaddress');
INSERT INTO public.auth_permission VALUES (42, 'Can change email address', 11, 'change_emailaddress');
INSERT INTO public.auth_permission VALUES (43, 'Can delete email address', 11, 'delete_emailaddress');
INSERT INTO public.auth_permission VALUES (44, 'Can view email address', 11, 'view_emailaddress');
INSERT INTO public.auth_permission VALUES (45, 'Can add email confirmation', 12, 'add_emailconfirmation');
INSERT INTO public.auth_permission VALUES (46, 'Can change email confirmation', 12, 'change_emailconfirmation');
INSERT INTO public.auth_permission VALUES (47, 'Can delete email confirmation', 12, 'delete_emailconfirmation');
INSERT INTO public.auth_permission VALUES (48, 'Can view email confirmation', 12, 'view_emailconfirmation');
INSERT INTO public.auth_permission VALUES (49, 'Can add social account', 13, 'add_socialaccount');
INSERT INTO public.auth_permission VALUES (50, 'Can change social account', 13, 'change_socialaccount');
INSERT INTO public.auth_permission VALUES (51, 'Can delete social account', 13, 'delete_socialaccount');
INSERT INTO public.auth_permission VALUES (52, 'Can view social account', 13, 'view_socialaccount');
INSERT INTO public.auth_permission VALUES (53, 'Can add social application', 14, 'add_socialapp');
INSERT INTO public.auth_permission VALUES (54, 'Can change social application', 14, 'change_socialapp');
INSERT INTO public.auth_permission VALUES (55, 'Can delete social application', 14, 'delete_socialapp');
INSERT INTO public.auth_permission VALUES (56, 'Can view social application', 14, 'view_socialapp');
INSERT INTO public.auth_permission VALUES (57, 'Can add social application token', 15, 'add_socialtoken');
INSERT INTO public.auth_permission VALUES (58, 'Can change social application token', 15, 'change_socialtoken');
INSERT INTO public.auth_permission VALUES (59, 'Can delete social application token', 15, 'delete_socialtoken');
INSERT INTO public.auth_permission VALUES (60, 'Can view social application token', 15, 'view_socialtoken');
INSERT INTO public.auth_permission VALUES (61, 'Can add User', 16, 'add_user');
INSERT INTO public.auth_permission VALUES (62, 'Can change User', 16, 'change_user');
INSERT INTO public.auth_permission VALUES (63, 'Can delete User', 16, 'delete_user');
INSERT INTO public.auth_permission VALUES (64, 'Can view User', 16, 'view_user');
INSERT INTO public.auth_permission VALUES (65, 'Can add User Profile', 17, 'add_userprofile');
INSERT INTO public.auth_permission VALUES (66, 'Can change User Profile', 17, 'change_userprofile');
INSERT INTO public.auth_permission VALUES (67, 'Can delete User Profile', 17, 'delete_userprofile');
INSERT INTO public.auth_permission VALUES (68, 'Can view User Profile', 17, 'view_userprofile');
INSERT INTO public.auth_permission VALUES (69, 'Can add Wishlist', 18, 'add_wishlist');
INSERT INTO public.auth_permission VALUES (70, 'Can change Wishlist', 18, 'change_wishlist');
INSERT INTO public.auth_permission VALUES (71, 'Can delete Wishlist', 18, 'delete_wishlist');
INSERT INTO public.auth_permission VALUES (72, 'Can view Wishlist', 18, 'view_wishlist');
INSERT INTO public.auth_permission VALUES (73, 'Can add Tour Category', 19, 'add_tourcategory');
INSERT INTO public.auth_permission VALUES (74, 'Can change Tour Category', 19, 'change_tourcategory');
INSERT INTO public.auth_permission VALUES (75, 'Can delete Tour Category', 19, 'delete_tourcategory');
INSERT INTO public.auth_permission VALUES (76, 'Can view Tour Category', 19, 'view_tourcategory');
INSERT INTO public.auth_permission VALUES (77, 'Can add Tour', 20, 'add_tour');
INSERT INTO public.auth_permission VALUES (78, 'Can change Tour', 20, 'change_tour');
INSERT INTO public.auth_permission VALUES (79, 'Can delete Tour', 20, 'delete_tour');
INSERT INTO public.auth_permission VALUES (80, 'Can view Tour', 20, 'view_tour');
INSERT INTO public.auth_permission VALUES (81, 'Can add Add-on', 21, 'add_addon');
INSERT INTO public.auth_permission VALUES (82, 'Can change Add-on', 21, 'change_addon');
INSERT INTO public.auth_permission VALUES (83, 'Can delete Add-on', 21, 'delete_addon');
INSERT INTO public.auth_permission VALUES (84, 'Can view Add-on', 21, 'view_addon');
INSERT INTO public.auth_permission VALUES (85, 'Can add Tour Departure', 22, 'add_tourdeparture');
INSERT INTO public.auth_permission VALUES (86, 'Can change Tour Departure', 22, 'change_tourdeparture');
INSERT INTO public.auth_permission VALUES (87, 'Can delete Tour Departure', 22, 'delete_tourdeparture');
INSERT INTO public.auth_permission VALUES (88, 'Can view Tour Departure', 22, 'view_tourdeparture');
INSERT INTO public.auth_permission VALUES (89, 'Can add Tour FAQ', 23, 'add_tourfaq');
INSERT INTO public.auth_permission VALUES (90, 'Can change Tour FAQ', 23, 'change_tourfaq');
INSERT INTO public.auth_permission VALUES (91, 'Can delete Tour FAQ', 23, 'delete_tourfaq');
INSERT INTO public.auth_permission VALUES (92, 'Can view Tour FAQ', 23, 'view_tourfaq');
INSERT INTO public.auth_permission VALUES (93, 'Can add Tour Highlight', 24, 'add_tourhighlight');
INSERT INTO public.auth_permission VALUES (94, 'Can change Tour Highlight', 24, 'change_tourhighlight');
INSERT INTO public.auth_permission VALUES (95, 'Can delete Tour Highlight', 24, 'delete_tourhighlight');
INSERT INTO public.auth_permission VALUES (96, 'Can view Tour Highlight', 24, 'view_tourhighlight');
INSERT INTO public.auth_permission VALUES (97, 'Can add Tour Image', 25, 'add_tourimage');
INSERT INTO public.auth_permission VALUES (98, 'Can change Tour Image', 25, 'change_tourimage');
INSERT INTO public.auth_permission VALUES (99, 'Can delete Tour Image', 25, 'delete_tourimage');
INSERT INTO public.auth_permission VALUES (100, 'Can view Tour Image', 25, 'view_tourimage');
INSERT INTO public.auth_permission VALUES (101, 'Can add Tour Inclusion', 26, 'add_tourinclusion');
INSERT INTO public.auth_permission VALUES (102, 'Can change Tour Inclusion', 26, 'change_tourinclusion');
INSERT INTO public.auth_permission VALUES (103, 'Can delete Tour Inclusion', 26, 'delete_tourinclusion');
INSERT INTO public.auth_permission VALUES (104, 'Can view Tour Inclusion', 26, 'view_tourinclusion');
INSERT INTO public.auth_permission VALUES (105, 'Can add Tour Itinerary', 27, 'add_touritinerary');
INSERT INTO public.auth_permission VALUES (106, 'Can change Tour Itinerary', 27, 'change_touritinerary');
INSERT INTO public.auth_permission VALUES (107, 'Can delete Tour Itinerary', 27, 'delete_touritinerary');
INSERT INTO public.auth_permission VALUES (108, 'Can view Tour Itinerary', 27, 'view_touritinerary');
INSERT INTO public.auth_permission VALUES (109, 'Can add Tour Pricing', 28, 'add_tourpricing');
INSERT INTO public.auth_permission VALUES (110, 'Can change Tour Pricing', 28, 'change_tourpricing');
INSERT INTO public.auth_permission VALUES (111, 'Can delete Tour Pricing', 28, 'delete_tourpricing');
INSERT INTO public.auth_permission VALUES (112, 'Can view Tour Pricing', 28, 'view_tourpricing');
INSERT INTO public.auth_permission VALUES (113, 'Can add Destination', 29, 'add_destination');
INSERT INTO public.auth_permission VALUES (114, 'Can change Destination', 29, 'change_destination');
INSERT INTO public.auth_permission VALUES (115, 'Can delete Destination', 29, 'delete_destination');
INSERT INTO public.auth_permission VALUES (116, 'Can view Destination', 29, 'view_destination');
INSERT INTO public.auth_permission VALUES (117, 'Can add Area', 30, 'add_area');
INSERT INTO public.auth_permission VALUES (118, 'Can change Area', 30, 'change_area');
INSERT INTO public.auth_permission VALUES (119, 'Can delete Area', 30, 'delete_area');
INSERT INTO public.auth_permission VALUES (120, 'Can view Area', 30, 'view_area');
INSERT INTO public.auth_permission VALUES (121, 'Can add Activity', 31, 'add_activity');
INSERT INTO public.auth_permission VALUES (122, 'Can change Activity', 31, 'change_activity');
INSERT INTO public.auth_permission VALUES (123, 'Can delete Activity', 31, 'delete_activity');
INSERT INTO public.auth_permission VALUES (124, 'Can view Activity', 31, 'view_activity');
INSERT INTO public.auth_permission VALUES (125, 'Can add Destination Image', 32, 'add_destinationimage');
INSERT INTO public.auth_permission VALUES (126, 'Can change Destination Image', 32, 'change_destinationimage');
INSERT INTO public.auth_permission VALUES (127, 'Can delete Destination Image', 32, 'delete_destinationimage');
INSERT INTO public.auth_permission VALUES (128, 'Can view Destination Image', 32, 'view_destinationimage');
INSERT INTO public.auth_permission VALUES (129, 'Can add Booking Add-on', 33, 'add_bookingaddon');
INSERT INTO public.auth_permission VALUES (130, 'Can change Booking Add-on', 33, 'change_bookingaddon');
INSERT INTO public.auth_permission VALUES (131, 'Can delete Booking Add-on', 33, 'delete_bookingaddon');
INSERT INTO public.auth_permission VALUES (132, 'Can view Booking Add-on', 33, 'view_bookingaddon');
INSERT INTO public.auth_permission VALUES (133, 'Can add Payment', 34, 'add_payment');
INSERT INTO public.auth_permission VALUES (134, 'Can change Payment', 34, 'change_payment');
INSERT INTO public.auth_permission VALUES (135, 'Can delete Payment', 34, 'delete_payment');
INSERT INTO public.auth_permission VALUES (136, 'Can view Payment', 34, 'view_payment');
INSERT INTO public.auth_permission VALUES (137, 'Can add Promo Code', 35, 'add_promocode');
INSERT INTO public.auth_permission VALUES (138, 'Can change Promo Code', 35, 'change_promocode');
INSERT INTO public.auth_permission VALUES (139, 'Can delete Promo Code', 35, 'delete_promocode');
INSERT INTO public.auth_permission VALUES (140, 'Can view Promo Code', 35, 'view_promocode');
INSERT INTO public.auth_permission VALUES (141, 'Can add Traveler', 36, 'add_traveler');
INSERT INTO public.auth_permission VALUES (142, 'Can change Traveler', 36, 'change_traveler');
INSERT INTO public.auth_permission VALUES (143, 'Can delete Traveler', 36, 'delete_traveler');
INSERT INTO public.auth_permission VALUES (144, 'Can view Traveler', 36, 'view_traveler');
INSERT INTO public.auth_permission VALUES (145, 'Can add Booking', 37, 'add_booking');
INSERT INTO public.auth_permission VALUES (146, 'Can change Booking', 37, 'change_booking');
INSERT INTO public.auth_permission VALUES (147, 'Can delete Booking', 37, 'delete_booking');
INSERT INTO public.auth_permission VALUES (148, 'Can view Booking', 37, 'view_booking');
INSERT INTO public.auth_permission VALUES (149, 'Can add Category', 38, 'add_category');
INSERT INTO public.auth_permission VALUES (150, 'Can change Category', 38, 'change_category');
INSERT INTO public.auth_permission VALUES (151, 'Can delete Category', 38, 'delete_category');
INSERT INTO public.auth_permission VALUES (152, 'Can view Category', 38, 'view_category');
INSERT INTO public.auth_permission VALUES (153, 'Can add Post', 39, 'add_post');
INSERT INTO public.auth_permission VALUES (154, 'Can change Post', 39, 'change_post');
INSERT INTO public.auth_permission VALUES (155, 'Can delete Post', 39, 'delete_post');
INSERT INTO public.auth_permission VALUES (156, 'Can view Post', 39, 'view_post');
INSERT INTO public.auth_permission VALUES (157, 'Can add Tag', 40, 'add_tag');
INSERT INTO public.auth_permission VALUES (158, 'Can change Tag', 40, 'change_tag');
INSERT INTO public.auth_permission VALUES (159, 'Can delete Tag', 40, 'delete_tag');
INSERT INTO public.auth_permission VALUES (160, 'Can view Tag', 40, 'view_tag');
INSERT INTO public.auth_permission VALUES (161, 'Can add Comment', 41, 'add_comment');
INSERT INTO public.auth_permission VALUES (162, 'Can change Comment', 41, 'change_comment');
INSERT INTO public.auth_permission VALUES (163, 'Can delete Comment', 41, 'delete_comment');
INSERT INTO public.auth_permission VALUES (164, 'Can view Comment', 41, 'view_comment');
INSERT INTO public.auth_permission VALUES (165, 'Can add Review Image', 42, 'add_reviewimage');
INSERT INTO public.auth_permission VALUES (166, 'Can change Review Image', 42, 'change_reviewimage');
INSERT INTO public.auth_permission VALUES (167, 'Can delete Review Image', 42, 'delete_reviewimage');
INSERT INTO public.auth_permission VALUES (168, 'Can view Review Image', 42, 'view_reviewimage');
INSERT INTO public.auth_permission VALUES (169, 'Can add Testimonial', 43, 'add_testimonial');
INSERT INTO public.auth_permission VALUES (170, 'Can change Testimonial', 43, 'change_testimonial');
INSERT INTO public.auth_permission VALUES (171, 'Can delete Testimonial', 43, 'delete_testimonial');
INSERT INTO public.auth_permission VALUES (172, 'Can view Testimonial', 43, 'view_testimonial');
INSERT INTO public.auth_permission VALUES (173, 'Can add Review', 44, 'add_review');
INSERT INTO public.auth_permission VALUES (174, 'Can change Review', 44, 'change_review');
INSERT INTO public.auth_permission VALUES (175, 'Can delete Review', 44, 'delete_review');
INSERT INTO public.auth_permission VALUES (176, 'Can view Review', 44, 'view_review');
INSERT INTO public.auth_permission VALUES (177, 'Can add FAQ', 45, 'add_faq');
INSERT INTO public.auth_permission VALUES (178, 'Can change FAQ', 45, 'change_faq');
INSERT INTO public.auth_permission VALUES (179, 'Can delete FAQ', 45, 'delete_faq');
INSERT INTO public.auth_permission VALUES (180, 'Can view FAQ', 45, 'view_faq');
INSERT INTO public.auth_permission VALUES (181, 'Can add Inquiry', 46, 'add_inquiry');
INSERT INTO public.auth_permission VALUES (182, 'Can change Inquiry', 46, 'change_inquiry');
INSERT INTO public.auth_permission VALUES (183, 'Can delete Inquiry', 46, 'delete_inquiry');
INSERT INTO public.auth_permission VALUES (184, 'Can view Inquiry', 46, 'view_inquiry');
INSERT INTO public.auth_permission VALUES (185, 'Can add Inquiry Response', 47, 'add_inquiryresponse');
INSERT INTO public.auth_permission VALUES (186, 'Can change Inquiry Response', 47, 'change_inquiryresponse');
INSERT INTO public.auth_permission VALUES (187, 'Can delete Inquiry Response', 47, 'delete_inquiryresponse');
INSERT INTO public.auth_permission VALUES (188, 'Can view Inquiry Response', 47, 'view_inquiryresponse');
INSERT INTO public.auth_permission VALUES (189, 'Can add Newsletter Subscriber', 48, 'add_newsletter');
INSERT INTO public.auth_permission VALUES (190, 'Can change Newsletter Subscriber', 48, 'change_newsletter');
INSERT INTO public.auth_permission VALUES (191, 'Can delete Newsletter Subscriber', 48, 'delete_newsletter');
INSERT INTO public.auth_permission VALUES (192, 'Can view Newsletter Subscriber', 48, 'view_newsletter');
INSERT INTO public.auth_permission VALUES (193, 'Can add Office', 49, 'add_office');
INSERT INTO public.auth_permission VALUES (194, 'Can change Office', 49, 'change_office');
INSERT INTO public.auth_permission VALUES (195, 'Can delete Office', 49, 'delete_office');
INSERT INTO public.auth_permission VALUES (196, 'Can view Office', 49, 'view_office');


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: blog_category; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: blog_post; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: blog_comment; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: destinations_destination; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.destinations_destination VALUES (1, '2025-12-06 14:07:33.31639-08', '2025-12-06 14:07:33.31639-08', 'cairo', '', '', '', 1, 'Cairo', 'القاهرة', 'Where History Comes Alive', 'Cairo, the sprawling capital of Egypt, is a city of contrasts where ancient wonders meet modern life. Home to the Great Pyramids of Giza and the Sphinx, Cairo offers visitors a journey through 5,000 years of history.', 'القاهرة، عاصمة مصر الممتدة، مدينة التناقضات حيث تلتقي العجائب القديمة بالحياة الحديثة.', '', '', '', 'Egypt', 'Lower Egypt', 30.044400, 31.235700, 'October to April when weather is cooler', '', '', true, true);
INSERT INTO public.destinations_destination VALUES (2, '2025-12-06 14:07:33.322393-08', '2025-12-06 14:07:33.322393-08', 'luxor', '', '', '', 2, 'Luxor', 'الأقصر', 'The World''s Greatest Open-Air Museum', 'Luxor, known as ancient Thebes, is home to some of Egypt''s most spectacular temples and tombs. The Valley of the Kings, Karnak Temple, and Luxor Temple await your discovery.', 'الأقصر، المعروفة بطيبة القديمة، موطن لبعض أروع المعابد والمقابر في مصر.', '', '', '', 'Egypt', 'Upper Egypt', 25.687200, 32.639600, 'October to March', '', '', true, true);
INSERT INTO public.destinations_destination VALUES (3, '2025-12-06 14:07:33.32738-08', '2025-12-06 14:07:33.32738-08', 'aswan', '', '', '', 3, 'Aswan', 'أسوان', 'Gateway to Nubia', 'Aswan offers a more relaxed atmosphere with beautiful Nile views, Nubian culture, and ancient temples including the magnificent Abu Simbel.', 'أسوان تقدم أجواء أكثر استرخاء مع إطلالات جميلة على النيل والثقافة النوبية.', '', '', '', 'Egypt', 'Upper Egypt', 24.088900, 32.899800, 'October to April', '', '', true, true);
INSERT INTO public.destinations_destination VALUES (4, '2025-12-06 14:07:33.331381-08', '2025-12-06 14:07:33.331381-08', 'sharm-el-sheikh', '', '', '', 4, 'Sharm El Sheikh', 'شرم الشيخ', 'Red Sea Paradise', 'Sharm El Sheikh is a world-renowned resort town on the Red Sea, famous for its crystal-clear waters, vibrant coral reefs, and year-round sunshine.', 'شرم الشيخ منتجع عالمي على البحر الأحمر، مشهور بمياهه الصافية والشعاب المرجانية.', '', '', '', 'Egypt', 'Sinai Peninsula', 27.915800, 34.330000, 'Year-round, best April to October', '', '', true, true);
INSERT INTO public.destinations_destination VALUES (5, '2025-12-06 14:07:33.3354-08', '2025-12-06 14:07:33.3354-08', 'alexandria', '', '', '', 5, 'Alexandria', 'الإسكندرية', 'Pearl of the Mediterranean', 'Alexandria, founded by Alexander the Great, blends ancient heritage with Mediterranean charm. Visit the modern Bibliotheca Alexandrina and historic Citadel of Qaitbay.', 'الإسكندرية، التي أسسها الإسكندر الأكبر، تمزج بين التراث القديم وسحر البحر المتوسط.', '', '', '', 'Egypt', 'Mediterranean Coast', 31.200100, 29.918700, 'March to May, September to November', '', '', false, true);


--
-- Data for Name: blog_post_related_destinations; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: tours_tourcategory; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_tourcategory VALUES (1, '2025-12-06 14:07:33.294388-08', '2025-12-06 14:07:33.294388-08', 'cultural-tours', 1, 'Cultural Tours', 'جولات ثقافية', 'Explore ancient history and rich culture', 'fa-landmark', '', true);
INSERT INTO public.tours_tourcategory VALUES (2, '2025-12-06 14:07:33.301387-08', '2025-12-06 14:07:33.301387-08', 'adventure-tours', 2, 'Adventure Tours', 'جولات مغامرات', 'Thrilling experiences and outdoor activities', 'fa-hiking', '', true);
INSERT INTO public.tours_tourcategory VALUES (3, '2025-12-06 14:07:33.306389-08', '2025-12-06 14:07:33.306389-08', 'beach-relax', 3, 'Beach & Relax', 'شواطئ واستجمام', 'Relax on beautiful beaches', 'fa-umbrella-beach', '', true);
INSERT INTO public.tours_tourcategory VALUES (4, '2025-12-06 14:07:33.31039-08', '2025-12-06 14:07:33.31039-08', 'nile-cruises', 4, 'Nile Cruises', 'رحلات نيلية', 'Cruise along the legendary Nile River', 'fa-ship', '', true);


--
-- Data for Name: tours_tour; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_tour VALUES (1, '2025-12-06 14:07:33.34338-08', '2025-12-06 14:07:33.34338-08', 'classic-egypt-tour', true, NULL, '', '', '', 'Classic Egypt Tour', 'جولة مصر الكلاسيكية', 'Discover the best of Egypt in 8 days including Cairo, Luxor, and Aswan', 'Experience the magic of Egypt on this comprehensive 8-day tour. Visit the iconic Pyramids of Giza, cruise the Nile River, explore ancient temples in Luxor, and discover Nubian culture in Aswan.

This carefully crafted itinerary covers all the must-see attractions while providing authentic cultural experiences. Travel in comfort with expert Egyptologist guides who bring history to life.

Highlights include the Great Pyramid, Sphinx, Valley of the Kings, Karnak Temple, and Abu Simbel. Perfect for first-time visitors to Egypt.', 'اكتشف سحر مصر في هذه الجولة الشاملة لمدة 8 أيام.', 'package', 8, 7, 1299.00, 350.00, 899.00, 'USD', 2, 16, '', '', true, true, false, true, 15, 4.8, 124, 'easy', 'Cairo', 'English, Spanish, French', 1);
INSERT INTO public.tours_tour VALUES (2, '2025-12-06 14:07:33.355385-08', '2025-12-06 14:07:33.355385-08', 'nile-cruise-adventure', true, NULL, '', '', '', 'Nile Cruise Adventure', 'مغامرة كروز النيل', '5-star Nile cruise from Luxor to Aswan with all temples included', 'Sail the legendary Nile River in style aboard a luxurious 5-star cruise ship. This 4-night journey from Luxor to Aswan takes you past timeless temples and traditional villages.

Enjoy premium accommodations, gourmet dining, and expert guided tours of ancient sites including Karnak, Luxor Temple, Edfu, Kom Ombo, and Philae Temple.

Relax on the sundeck as the Egyptian landscape unfolds before you, creating memories that will last a lifetime.', 'أبحر في نهر النيل الأسطوري بأناقة على متن سفينة فاخرة 5 نجوم.', 'nile_cruise', 5, 4, 899.00, 250.00, 599.00, 'USD', 2, 50, '', '', true, true, false, false, NULL, 4.9, 89, 'easy', 'Luxor', 'English, German, French', 4);
INSERT INTO public.tours_tour VALUES (3, '2025-12-06 14:07:33.363383-08', '2025-12-06 14:07:33.363383-08', 'red-sea-diving-experience', true, NULL, '', '', '', 'Red Sea Diving Experience', 'تجربة الغوص في البحر الأحمر', '7-day diving adventure in Sharm El Sheikh with PADI certification', 'Dive into the crystal-clear waters of the Red Sea on this 7-day diving adventure. Sharm El Sheikh offers some of the world''s best dive sites with vibrant coral reefs and diverse marine life.

Whether you''re a beginner or experienced diver, this package includes PADI certification courses, guided dives, and free time to explore the resort.

Highlights include Ras Mohammed National Park, Tiran Island, and the famous SS Thistlegorm wreck.', 'انغمس في المياه الصافية للبحر الأحمر في هذه المغامرة لمدة 7 أيام.', 'package', 7, 6, 1099.00, 300.00, NULL, 'USD', 1, 12, '', '', true, false, true, true, 10, 4.7, 56, 'moderate', 'Sharm El Sheikh', 'English, Russian', 2);
INSERT INTO public.tours_tour VALUES (4, '2025-12-06 14:07:33.371387-08', '2025-12-06 14:07:33.371387-08', 'cairo-day-tour', true, NULL, '', '', '', 'Cairo Day Tour', 'جولة القاهرة اليومية', 'Full day tour of Cairo''s highlights including Pyramids and Egyptian Museum', 'Make the most of your time in Cairo with this comprehensive day tour covering all major attractions. Visit the legendary Pyramids of Giza and Sphinx, explore the treasures of the Egyptian Museum, and experience the vibrant Khan El Khalili bazaar.

Includes hotel pickup, professional Egyptologist guide, entrance fees, and traditional Egyptian lunch.

Perfect for travelers with limited time who want to see Cairo''s best.', 'استفد من وقتك في القاهرة مع هذه الجولة الشاملة.', 'day_tour', 1, 0, 89.00, NULL, 59.00, 'USD', 1, 15, '', '', false, true, false, false, NULL, 4.6, 234, 'easy', 'Cairo', 'English, Spanish, French, German, Italian', 1);
INSERT INTO public.tours_tour VALUES (5, '2025-12-06 14:07:33.378386-08', '2025-12-06 14:07:33.378386-08', 'sharm-beach-retreat', true, NULL, '', '', '', 'Sharm Beach Retreat', 'استجمام شرم الشاطئي', '5-day all-inclusive beach vacation at 5-star resort', 'Escape to paradise at a luxury 5-star beachfront resort in Sharm El Sheikh. This all-inclusive package offers the perfect blend of relaxation and activities.

Enjoy private beach access, world-class spa treatments, water sports, and exceptional dining. Optional excursions include snorkeling trips, desert safaris, and visits to Mount Sinai.

Ideal for couples, families, and anyone seeking a rejuvenating beach holiday.', 'اهرب إلى الجنة في منتجع فاخر 5 نجوم على الشاطئ في شرم الشيخ.', 'package', 5, 4, 699.00, 200.00, 399.00, 'USD', 1, 50, '', '', true, false, true, true, 20, 4.5, 78, 'easy', 'Sharm El Sheikh', 'English, Russian, German', 3);
INSERT INTO public.tours_tour VALUES (6, '2025-12-06 14:07:33.385388-08', '2025-12-06 14:07:33.385388-08', 'alexandria-day-trip', true, NULL, '', '', '', 'Alexandria Day Trip', 'رحلة يومية إلى الإسكندرية', 'Explore the Mediterranean gem of Alexandria from Cairo', 'Discover the charm of Alexandria on this full-day excursion from Cairo. Visit the stunning Bibliotheca Alexandrina, the historic Citadel of Qaitbay, and the mysterious Catacombs of Kom El Shoqafa.

Enjoy a seafood lunch with Mediterranean views and stroll along the famous Corniche. This day trip offers a perfect escape from Cairo and a glimpse into Egypt''s Greek and Roman heritage.', 'اكتشف سحر الإسكندرية في هذه الرحلة اليومية من القاهرة.', 'day_tour', 1, 0, 79.00, NULL, 49.00, 'USD', 2, 20, '', '', false, false, false, false, NULL, 4.4, 67, 'easy', 'Cairo', 'English, French', 1);


--
-- Data for Name: blog_post_related_tours; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: blog_tag; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: blog_post_tags; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: tours_tourdeparture; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: bookings_booking; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: tours_addon; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: bookings_bookingaddon; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: bookings_promocode; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: bookings_promocode_applicable_tours; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: bookings_traveler; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: contact_faq; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: contact_inquiry; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: contact_inquiryresponse; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: contact_newsletter; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: contact_office; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: destinations_activity; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.destinations_activity VALUES (1, '2025-12-06 14:07:33.454386-08', '2025-12-06 14:07:33.454386-08', 0, 'Pyramids Sound & Light Show', 'Spectacular evening show at the Pyramids', '', 35.00, NULL, '2 hours', 1);
INSERT INTO public.destinations_activity VALUES (2, '2025-12-06 14:07:33.458387-08', '2025-12-06 14:07:33.458387-08', 0, 'Felucca Ride on the Nile', 'Traditional sailboat cruise at sunset', '', 25.00, NULL, '1.5 hours', 1);
INSERT INTO public.destinations_activity VALUES (3, '2025-12-06 14:07:33.462394-08', '2025-12-06 14:07:33.462394-08', 0, 'Hot Air Balloon Ride', 'Sunrise balloon flight over Valley of the Kings', '', 95.00, NULL, '3 hours', 2);
INSERT INTO public.destinations_activity VALUES (4, '2025-12-06 14:07:33.466388-08', '2025-12-06 14:07:33.466388-08', 0, 'Snorkeling Trip', 'Visit top snorkeling spots in the Red Sea', '', 45.00, NULL, 'Full day', 4);
INSERT INTO public.destinations_activity VALUES (5, '2025-12-06 14:07:33.471391-08', '2025-12-06 14:07:33.471391-08', 0, 'Desert Safari', 'Quad biking and Bedouin dinner in the desert', '', 65.00, NULL, '5 hours', 4);


--
-- Data for Name: destinations_area; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: destinations_destinationimage; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_migrations VALUES (1, 'destinations', '0001_initial', '2025-12-06 13:38:59.855729-08');
INSERT INTO public.django_migrations VALUES (2, 'tours', '0001_initial', '2025-12-06 13:39:00.157407-08');
INSERT INTO public.django_migrations VALUES (3, 'contenttypes', '0001_initial', '2025-12-06 13:39:00.176407-08');
INSERT INTO public.django_migrations VALUES (4, 'contenttypes', '0002_remove_content_type_name', '2025-12-06 13:39:00.201001-08');
INSERT INTO public.django_migrations VALUES (5, 'auth', '0001_initial', '2025-12-06 13:39:00.255788-08');
INSERT INTO public.django_migrations VALUES (6, 'auth', '0002_alter_permission_name_max_length', '2025-12-06 13:39:00.263754-08');
INSERT INTO public.django_migrations VALUES (7, 'auth', '0003_alter_user_email_max_length', '2025-12-06 13:39:00.269745-08');
INSERT INTO public.django_migrations VALUES (8, 'auth', '0004_alter_user_username_opts', '2025-12-06 13:39:00.275745-08');
INSERT INTO public.django_migrations VALUES (9, 'auth', '0005_alter_user_last_login_null', '2025-12-06 13:39:00.281746-08');
INSERT INTO public.django_migrations VALUES (10, 'auth', '0006_require_contenttypes_0002', '2025-12-06 13:39:00.283742-08');
INSERT INTO public.django_migrations VALUES (11, 'auth', '0007_alter_validators_add_error_messages', '2025-12-06 13:39:00.289738-08');
INSERT INTO public.django_migrations VALUES (12, 'auth', '0008_alter_user_username_max_length', '2025-12-06 13:39:00.296878-08');
INSERT INTO public.django_migrations VALUES (13, 'auth', '0009_alter_user_last_name_max_length', '2025-12-06 13:39:00.302908-08');
INSERT INTO public.django_migrations VALUES (14, 'auth', '0010_alter_group_name_max_length', '2025-12-06 13:39:00.310888-08');
INSERT INTO public.django_migrations VALUES (15, 'auth', '0011_update_proxy_permissions', '2025-12-06 13:39:00.330888-08');
INSERT INTO public.django_migrations VALUES (16, 'auth', '0012_alter_user_first_name_max_length', '2025-12-06 13:39:00.342887-08');
INSERT INTO public.django_migrations VALUES (17, 'users', '0001_initial', '2025-12-06 13:39:00.491635-08');
INSERT INTO public.django_migrations VALUES (18, 'account', '0001_initial', '2025-12-06 13:39:00.575475-08');
INSERT INTO public.django_migrations VALUES (19, 'account', '0002_email_max_length', '2025-12-06 13:39:00.590476-08');
INSERT INTO public.django_migrations VALUES (20, 'account', '0003_alter_emailaddress_create_unique_verified_email', '2025-12-06 13:39:00.617501-08');
INSERT INTO public.django_migrations VALUES (21, 'account', '0004_alter_emailaddress_drop_unique_email', '2025-12-06 13:39:00.63702-08');
INSERT INTO public.django_migrations VALUES (22, 'account', '0005_emailaddress_idx_upper_email', '2025-12-06 13:39:00.652012-08');
INSERT INTO public.django_migrations VALUES (23, 'admin', '0001_initial', '2025-12-06 13:39:00.726011-08');
INSERT INTO public.django_migrations VALUES (24, 'admin', '0002_logentry_remove_auto_add', '2025-12-06 13:39:00.742022-08');
INSERT INTO public.django_migrations VALUES (25, 'admin', '0003_logentry_add_action_flag_choices', '2025-12-06 13:39:00.761008-08');
INSERT INTO public.django_migrations VALUES (26, 'authtoken', '0001_initial', '2025-12-06 13:39:00.804921-08');
INSERT INTO public.django_migrations VALUES (27, 'authtoken', '0002_auto_20160226_1747', '2025-12-06 13:39:00.872917-08');
INSERT INTO public.django_migrations VALUES (28, 'authtoken', '0003_tokenproxy', '2025-12-06 13:39:00.876922-08');
INSERT INTO public.django_migrations VALUES (29, 'blog', '0001_initial', '2025-12-06 13:39:00.950919-08');
INSERT INTO public.django_migrations VALUES (30, 'blog', '0002_initial', '2025-12-06 13:39:01.245548-08');
INSERT INTO public.django_migrations VALUES (31, 'bookings', '0001_initial', '2025-12-06 13:39:01.353586-08');
INSERT INTO public.django_migrations VALUES (32, 'bookings', '0002_initial', '2025-12-06 13:39:01.725896-08');
INSERT INTO public.django_migrations VALUES (33, 'contact', '0001_initial', '2025-12-06 13:39:01.787845-08');
INSERT INTO public.django_migrations VALUES (34, 'contact', '0002_initial', '2025-12-06 13:39:01.973654-08');
INSERT INTO public.django_migrations VALUES (35, 'reviews', '0001_initial', '2025-12-06 13:39:02.061681-08');
INSERT INTO public.django_migrations VALUES (36, 'reviews', '0002_initial', '2025-12-06 13:39:02.208629-08');
INSERT INTO public.django_migrations VALUES (37, 'sessions', '0001_initial', '2025-12-06 13:39:02.223252-08');
INSERT INTO public.django_migrations VALUES (38, 'sites', '0001_initial', '2025-12-06 13:39:02.231244-08');
INSERT INTO public.django_migrations VALUES (39, 'sites', '0002_alter_domain_unique', '2025-12-06 13:39:02.241783-08');
INSERT INTO public.django_migrations VALUES (40, 'socialaccount', '0001_initial', '2025-12-06 13:39:02.460201-08');
INSERT INTO public.django_migrations VALUES (41, 'socialaccount', '0002_token_max_lengths', '2025-12-06 13:39:02.604236-08');
INSERT INTO public.django_migrations VALUES (42, 'socialaccount', '0003_extra_data_default_dict', '2025-12-06 13:39:02.630424-08');
INSERT INTO public.django_migrations VALUES (43, 'socialaccount', '0004_app_provider_id_settings', '2025-12-06 13:39:02.676023-08');
INSERT INTO public.django_migrations VALUES (44, 'socialaccount', '0005_socialtoken_nullable_app', '2025-12-06 13:39:02.74602-08');
INSERT INTO public.django_migrations VALUES (45, 'socialaccount', '0006_alter_socialaccount_extra_data', '2025-12-06 13:39:02.781822-08');
INSERT INTO public.django_migrations VALUES (46, 'token_blacklist', '0001_initial', '2025-12-06 13:39:02.927076-08');
INSERT INTO public.django_migrations VALUES (47, 'token_blacklist', '0002_outstandingtoken_jti_hex', '2025-12-06 13:39:02.95507-08');
INSERT INTO public.django_migrations VALUES (48, 'token_blacklist', '0003_auto_20171017_2007', '2025-12-06 13:39:03.008075-08');
INSERT INTO public.django_migrations VALUES (49, 'token_blacklist', '0004_auto_20171017_2013', '2025-12-06 13:39:03.047073-08');
INSERT INTO public.django_migrations VALUES (50, 'token_blacklist', '0005_remove_outstandingtoken_jti', '2025-12-06 13:39:03.078174-08');
INSERT INTO public.django_migrations VALUES (51, 'token_blacklist', '0006_auto_20171017_2113', '2025-12-06 13:39:03.110651-08');
INSERT INTO public.django_migrations VALUES (52, 'token_blacklist', '0007_auto_20171017_2214', '2025-12-06 13:39:03.196638-08');
INSERT INTO public.django_migrations VALUES (53, 'token_blacklist', '0008_migrate_to_bigautofield', '2025-12-06 13:39:03.299471-08');
INSERT INTO public.django_migrations VALUES (54, 'token_blacklist', '0010_fix_migrate_to_bigautofield', '2025-12-06 13:39:03.360459-08');
INSERT INTO public.django_migrations VALUES (55, 'token_blacklist', '0011_linearizes_history', '2025-12-06 13:39:03.364154-08');
INSERT INTO public.django_migrations VALUES (56, 'token_blacklist', '0012_alter_outstandingtoken_user', '2025-12-06 13:39:03.500697-08');
INSERT INTO public.django_migrations VALUES (57, 'bookings', '0003_remove_booking_payment_status_delete_payment', '2025-12-07 05:18:10.669025-08');


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_site VALUES (1, 'example.com', 'example.com');


--
-- Data for Name: reviews_review; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: reviews_reviewimage; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: reviews_testimonial; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: socialaccount_socialaccount; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: socialaccount_socialapp; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: socialaccount_socialapp_sites; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: socialaccount_socialtoken; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: token_blacklist_outstandingtoken; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: token_blacklist_blacklistedtoken; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: tours_addon_tours; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: tours_tour_destinations; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_tour_destinations VALUES (1, 1, 1);
INSERT INTO public.tours_tour_destinations VALUES (2, 1, 2);
INSERT INTO public.tours_tour_destinations VALUES (3, 1, 3);
INSERT INTO public.tours_tour_destinations VALUES (4, 2, 2);
INSERT INTO public.tours_tour_destinations VALUES (5, 2, 3);
INSERT INTO public.tours_tour_destinations VALUES (6, 3, 4);
INSERT INTO public.tours_tour_destinations VALUES (7, 4, 1);
INSERT INTO public.tours_tour_destinations VALUES (8, 5, 4);
INSERT INTO public.tours_tour_destinations VALUES (9, 6, 5);


--
-- Data for Name: tours_tourfaq; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: tours_tourhighlight; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_tourhighlight VALUES (1, '2025-12-06 14:07:33.393398-08', '2025-12-06 14:07:33.393398-08', 1, 'Great Pyramids of Giza', 'Marvel at the last remaining wonder of the ancient world', 'fa-monument', 1);
INSERT INTO public.tours_tourhighlight VALUES (2, '2025-12-06 14:07:33.397383-08', '2025-12-06 14:07:33.397383-08', 2, 'Valley of the Kings', 'Explore ancient royal tombs including Tutankhamun', 'fa-crown', 1);
INSERT INTO public.tours_tourhighlight VALUES (3, '2025-12-06 14:07:33.401384-08', '2025-12-06 14:07:33.401384-08', 3, 'Nile River Cruise', 'Sail the legendary river in luxury', 'fa-ship', 1);
INSERT INTO public.tours_tourhighlight VALUES (4, '2025-12-06 14:07:33.405389-08', '2025-12-06 14:07:33.405389-08', 4, 'Abu Simbel Temples', 'Witness the colossal temples of Ramesses II', 'fa-temple', 1);


--
-- Data for Name: tours_tourimage; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: tours_tourinclusion; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_tourinclusion VALUES (1, '2025-12-06 14:07:33.409384-08', '2025-12-06 14:07:33.409384-08', 1, 'All domestic flights', true, 1);
INSERT INTO public.tours_tourinclusion VALUES (2, '2025-12-06 14:07:33.413383-08', '2025-12-06 14:07:33.413383-08', 2, '7 nights accommodation', true, 1);
INSERT INTO public.tours_tourinclusion VALUES (3, '2025-12-06 14:07:33.416391-08', '2025-12-06 14:07:33.416391-08', 3, 'Daily breakfast and select meals', true, 1);
INSERT INTO public.tours_tourinclusion VALUES (4, '2025-12-06 14:07:33.420398-08', '2025-12-06 14:07:33.420398-08', 4, 'Professional Egyptologist guide', true, 1);
INSERT INTO public.tours_tourinclusion VALUES (5, '2025-12-06 14:07:33.423388-08', '2025-12-06 14:07:33.423388-08', 5, 'All entrance fees', true, 1);
INSERT INTO public.tours_tourinclusion VALUES (6, '2025-12-06 14:07:33.426386-08', '2025-12-06 14:07:33.426386-08', 6, 'Airport transfers', true, 1);
INSERT INTO public.tours_tourinclusion VALUES (7, '2025-12-06 14:07:33.429403-08', '2025-12-06 14:07:33.429403-08', 7, 'International flights', false, 1);
INSERT INTO public.tours_tourinclusion VALUES (8, '2025-12-06 14:07:33.43438-08', '2025-12-06 14:07:33.43438-08', 8, 'Travel insurance', false, 1);
INSERT INTO public.tours_tourinclusion VALUES (9, '2025-12-06 14:07:33.438381-08', '2025-12-06 14:07:33.438381-08', 9, 'Personal expenses', false, 1);


--
-- Data for Name: tours_touritinerary; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tours_touritinerary VALUES (1, '2025-12-06 14:07:33.442386-08', '2025-12-06 14:07:33.442386-08', 1, 1, 'Welcome to Cairo', 'Arrive at Cairo International Airport where you will be met by our representative. Transfer to your hotel for check-in and rest. Evening welcome dinner with traditional Egyptian cuisine.', 'Cairo', 'Dinner', '5-star hotel in Cairo', '', 1);
INSERT INTO public.tours_touritinerary VALUES (2, '2025-12-06 14:07:33.446386-08', '2025-12-06 14:07:33.446386-08', 2, 2, 'Pyramids & Sphinx', 'Full day exploring the Giza Plateau. Visit the Great Pyramid, Sphinx, and Valley Temple. Optional camel ride. Afternoon visit to the Egyptian Museum.', 'Giza, Cairo', 'Breakfast, Lunch', '5-star hotel in Cairo', '', 1);
INSERT INTO public.tours_touritinerary VALUES (3, '2025-12-06 14:07:33.449384-08', '2025-12-06 14:07:33.449384-08', 3, 3, 'Fly to Luxor', 'Morning flight to Luxor. Visit Karnak Temple, the largest ancient religious site in the world. Evening sound and light show.', 'Luxor', 'Breakfast, Dinner', 'Nile cruise ship', '', 1);


--
-- Data for Name: tours_tourpricing; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: users_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: users_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: users_userprofile; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: users_wishlist; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.account_emailaddress_id_seq', 1, false);


--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.account_emailconfirmation_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 196, true);


--
-- Name: blog_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blog_category_id_seq', 1, false);


--
-- Name: blog_comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blog_comment_id_seq', 1, false);


--
-- Name: blog_post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blog_post_id_seq', 1, false);


--
-- Name: blog_post_related_destinations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blog_post_related_destinations_id_seq', 1, false);


--
-- Name: blog_post_related_tours_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blog_post_related_tours_id_seq', 1, false);


--
-- Name: blog_post_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blog_post_tags_id_seq', 1, false);


--
-- Name: blog_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blog_tag_id_seq', 1, false);


--
-- Name: bookings_booking_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bookings_booking_id_seq', 1, false);


--
-- Name: bookings_bookingaddon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bookings_bookingaddon_id_seq', 1, false);


--
-- Name: bookings_promocode_applicable_tours_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bookings_promocode_applicable_tours_id_seq', 1, false);


--
-- Name: bookings_promocode_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bookings_promocode_id_seq', 1, false);


--
-- Name: bookings_traveler_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bookings_traveler_id_seq', 1, false);


--
-- Name: contact_faq_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contact_faq_id_seq', 1, false);


--
-- Name: contact_inquiry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contact_inquiry_id_seq', 1, false);


--
-- Name: contact_inquiryresponse_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contact_inquiryresponse_id_seq', 1, false);


--
-- Name: contact_newsletter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contact_newsletter_id_seq', 1, false);


--
-- Name: contact_office_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contact_office_id_seq', 1, false);


--
-- Name: destinations_activity_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.destinations_activity_id_seq', 5, true);


--
-- Name: destinations_area_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.destinations_area_id_seq', 1, false);


--
-- Name: destinations_destination_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.destinations_destination_id_seq', 5, true);


--
-- Name: destinations_destinationimage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.destinations_destinationimage_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 49, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 57, true);


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_site_id_seq', 1, true);


--
-- Name: reviews_review_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reviews_review_id_seq', 1, false);


--
-- Name: reviews_reviewimage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reviews_reviewimage_id_seq', 1, false);


--
-- Name: reviews_testimonial_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reviews_testimonial_id_seq', 1, false);


--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialaccount_id_seq', 1, false);


--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialapp_id_seq', 1, false);


--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialapp_sites_id_seq', 1, false);


--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialtoken_id_seq', 1, false);


--
-- Name: token_blacklist_blacklistedtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.token_blacklist_blacklistedtoken_id_seq', 1, false);


--
-- Name: token_blacklist_outstandingtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.token_blacklist_outstandingtoken_id_seq', 1, false);


--
-- Name: tours_addon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_addon_id_seq', 1, false);


--
-- Name: tours_addon_tours_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_addon_tours_id_seq', 1, false);


--
-- Name: tours_tour_destinations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_tour_destinations_id_seq', 9, true);


--
-- Name: tours_tour_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_tour_id_seq', 6, true);


--
-- Name: tours_tourcategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_tourcategory_id_seq', 4, true);


--
-- Name: tours_tourdeparture_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_tourdeparture_id_seq', 1, false);


--
-- Name: tours_tourfaq_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_tourfaq_id_seq', 1, false);


--
-- Name: tours_tourhighlight_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_tourhighlight_id_seq', 4, true);


--
-- Name: tours_tourimage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_tourimage_id_seq', 1, false);


--
-- Name: tours_tourinclusion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_tourinclusion_id_seq', 9, true);


--
-- Name: tours_touritinerary_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_touritinerary_id_seq', 3, true);


--
-- Name: tours_tourpricing_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tours_tourpricing_id_seq', 1, false);


--
-- Name: users_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_user_groups_id_seq', 1, false);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_user_id_seq', 1, false);


--
-- Name: users_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_user_user_permissions_id_seq', 1, false);


--
-- Name: users_userprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_userprofile_id_seq', 1, false);


--
-- Name: users_wishlist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_wishlist_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

