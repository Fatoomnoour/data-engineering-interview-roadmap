# اختبار تحديد المستوى

أجب عن الأسئلة التالية كتابةً، ثم نفّذ تمرين المستوى الذي تعتقد أنك جاهز له. لا تستخدم النتيجة كحكم نهائي؛ الهدف هو اكتشاف الفجوات.

| إذا استطعت أن… | ابدأ غالباً من… |
|---|---|
| تكتب برنامج Python بسيطاً، وتستخدم terminal، وتشرح primary key وJOIN | Level 0 |
| تبني extractor من API، وتستخدم Docker/PostgreSQL، وتكتب tests وrerun آمن | Level 1 |
| تصمم star schema، وتشرح grain وSCD، وتبني dbt models وAirflow DAG | Level 2 |
| تشرح shuffle وpartitioning وwatermark وconsumer groups وتنفذ replay | Level 3 |
| تقدر على estimates وSLOs وcost/failure/security trade-offs وتدافع عن ADR | Level 4 |

## أسئلة تحقق قصيرة

اكتب إجابة من فقرة لكل سؤال. إذا احتجت إلى حفظ تعريف، عد إلى المستوى السابق.

1. ما الفرق بين `WHERE` و`HAVING`، ومتى قد تنتج `JOIN` صفوفاً مكررة؟
2. كيف تجعل تحميل ملف أو صفحة API idempotent؟
3. ما الـ grain في fact table لمعاملات متجر إلكتروني؟
4. متى تختار full refresh ومتى تختار incremental load؟
5. ماذا يعني أن transformation في Spark تسبب shuffle؟
6. كيف تتعامل مع حدث يصل بعد إغلاق نافذة زمنية؟
7. ما الفرق بين retry وbackfill وreplay؟
8. ما المعلومات التي تحتاجها قبل اختيار batch أو streaming؟
9. كيف تمنع PII من الوصول إلى طبقة analytics؟
10. كيف تثبت أن pipeline «نجحت» غير مجرد أنها لم ترجع error؟

## بوابة الانتقال

انتقل إلى المستوى التالي فقط عندما تستطيع: تنفيذ مشروع صغير دون tutorial خطوة بخطوة، كتابة اختبار لفشل متوقع، شرح تصميمك خلال خمس دقائق، وكتابة README يعيد شخص آخر تشغيله. إذا فشلت في واحدة من هذه، لا تعتبر ذلك تراجعاً؛ اعتبره task واضحاً للمرحلة الحالية.
