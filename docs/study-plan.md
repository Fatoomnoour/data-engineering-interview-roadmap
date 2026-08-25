# خطة مذاكرة 16 أسبوعاً

الخطة مبنية على 8–10 ساعات أسبوعياً. إذا كان وقتك أقل، حافظ على ترتيب الوحدات ومدد المدة؛ لا تختصر المشاريع بإزالة الاختبارات والتوثيق. كل أسبوع يتكون من قراءة قصيرة، تنفيذ، ثم مراجعة بصوت عالٍ.

| الأسابيع | التركيز | المخرج |
|---|---|---|
| 1–2 | Linux، Git، Python basics، virtual environments | CLI notes + Python utilities |
| 3–4 | SQL fundamentals، joins، CTEs، windows، NULL، dates | 40 SQL solutions مع شرح grain |
| 5 | PostgreSQL، indexes، transactions، EXPLAIN، HTTP/APIs | API extractor موثق |
| 6 | Docker وCompose، logging، configuration، testing | خدمة محلية قابلة لإعادة التشغيل |
| 7–8 | Batch ETL وincremental loading وidempotency | مشروع 01 من المصدر إلى database |
| 9 | Dimensional modeling، facts/dimensions، SCD، data contracts | ERD + star schema + sample queries |
| 10–11 | Warehouse، dbt، tests، docs، incremental models | مشروع 02 transformations وquality |
| 12 | Airflow، DAG design، retries، backfill، SLA/freshness | DAG + runbook + failure drill |
| 13 | Spark/PySpark، partitions، joins، shuffle، Parquet | benchmark صغير قبل/بعد optimization |
| 14 | Kafka/streaming، offsets، replay، event time، dedup | event producer/consumer |
| 15 | System design، security، observability، cost | architecture document + ADRs |
| 16 | Mock interviews وportfolio polish | مقابلة تجريبية + نسخة نهائية من GitHub |

## شكل الأسبوع

خصص جلستين للمفهوم، وثلاث جلسات للكود، وجلسة لاختبار failure أو تحسين الأداء، وجلسة أخيرة لشرح ما بنيته كأنك في مقابلة. في نهاية الأسبوع اكتب ثلاثة أسطر: ما الذي فهمته؟ ما الذي فشل؟ وما القرار الذي ستغيره؟

## خطة المراجعة قبل المقابلة

في آخر 14 يوماً، حل SQL يومياً، واكتب design prompt كل يومين، ونفّذ debugging drill مرة أسبوعياً. لا تحفظ إجابات الشركات؛ درّب نفسك على توضيح الافتراضات، تقدير الحجم، اختيار التخزين، ومناقشة backfill وlate data وcost.

## مؤشرات التقدم

| المؤشر | الهدف النهائي |
|---|---:|
| مسائل SQL مشروحة | 60 |
| مشاريع end-to-end | 3 |
| اختبارات automated | موجودة في كل مشروع |
| system designs مكتوبة | 8 |
| STAR stories مسجلة | 6 |
| mock interviews | 4 |

## مبدأ مهم

الوقت لا يقاس بعدد الفيديوهات. يقاس بعدد المرات التي استطعت فيها تشغيل pipeline من الصفر، كسرها عمداً، قراءة الخطأ، إصلاحها، وإقناع شخص آخر بأن التصميم آمن وقابل للتوسع.
