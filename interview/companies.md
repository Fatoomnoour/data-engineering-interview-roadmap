# الشركات المستهدفة واستراتيجية التقديم

هذه قائمة تدريب وليست وعداً بأن كل وظيفة في الشركة لها نفس المقابلة. الوظائف والـ stack تتغير حسب الفريق والمستوى والموقع؛ لذلك اقرأ الوصف الحالي للوظيفة، وابحث عن اسم الفريق، ثم عدّل مشروعك وسيرتك الذاتية وفق المتطلبات الفعلية.

## تصنيف عملي

| نوع الشركة | أمثلة للبحث | ما الذي تبرهنه في المقابلة |
|---|---|---|
| Big Tech وconsumer scale | Google، Meta، Amazon، Netflix | SQL قوي، distributed systems، scale estimates، reliability، behavioral ownership |
| Marketplace وmobility | Uber، DoorDash، Careem | event streams، geospatial/business events، data quality، freshness، experimentation |
| Data platforms | Databricks، Snowflake، Confluent | Spark/warehouse internals، query performance، storage formats، APIs، trade-offs |
| Fintech وenterprise | Microsoft، Stripe، Wise، SAP | correctness، security، auditability، SLAs، schema evolution، privacy |
| Startups وremote teams | ابحث في Wellfound، LinkedIn، مواقع الشركات | ownership، سرعة الشحن، Python/SQL breadth، cloud pragmatism، تشغيل end-to-end |

## كيف تبني ملفاً مناسباً

للوظائف التي تركز على analytics engineering، اجعل مشروع warehouse/dbt هو الواجهة. لو كانت الوظيفة platform أو big data، اعرض Spark وpartitioning وobservability. لو كانت streaming، اجعل replay وoffsets وlate data واضحة. لو كانت fintech، أبرز constraints وaudit trail وPII masking بدلاً من التركيز على عدد الأدوات.

## خطة التقديم

أنشئ جدول متابعة يحتوي على الشركة، الوظيفة، المستوى، الموقع، تاريخ النشر، المهارات المطلوبة، مصدر الإحالة، ونسخة السيرة المستخدمة. لا ترسل نسخة عامة لكل الوظائف؛ اختر ثلاثة أدلة من الوصف واصنع لكل دليل bullet في السيرة أو رابطاً من مشروعك.

## مصادر البحث عن نمط المقابلة

يضم [Data Engineering Interview Handbook](https://github.com/datadriven-io/data-engineering-interview-handbook) أدلة تدريبية مرتبطة بـ Netflix وUber وAmazon وGoogle وMeta. استخدمه كفهرس موضوعات، ثم تحقق من المعلومات في صفحة الوظيفة الحالية وموقع careers الرسمي للشركة، لأن تجارب المقابلات المنشورة قديمة أو خاصة بفريق واحد.

## تحذير من المقارنة السطحية

لا تقارن الشركات بعدد الأدوات المذكورة في الوصف فقط. قارن درجة ownership، نوع البيانات، حجم النظام، on-call، cloud، فرص التعلم، وطبيعة المنتج. هدف الريبو أن يثبت طريقة التفكير التي تنتقل بين الشركات، لا أن يطارد كلمة مفتاحية واحدة.
