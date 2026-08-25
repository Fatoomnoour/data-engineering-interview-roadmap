# المشاريع العملية

كل مشروع هنا مصمم ليكون قطعة Portfolio، لا تمريناً معزولاً. استخدم بيانات عامة لا تحتوي على معلومات شخصية، وثبّت نسخة الأدوات، وأرفق طريقة تشغيل reproducible. لا تكتب «built a pipeline» فقط؛ اذكر حجم البيانات، freshness، اختبارات الجودة، وأي trade-off.

## Project 01 — API to PostgreSQL Batch Pipeline

**المستوى:** Junior. اسحب بيانات من API عامة ذات pagination، احفظ raw responses، طبّق schema validation، ثم حمّل staging وanalytics tables في PostgreSQL عبر Docker Compose.

**المتطلبات:** retry with exponential backoff، rate-limit handling، idempotent load، `loaded_at` و`source_updated_at`، logging، unit tests، integration test، وMakefile أو أوامر واضحة. أضف سيناريو duplicate input وسيناريو API failure.

**أسئلة المقابلة التي يثبتها:** كيف تمنع التكرار؟ ماذا تفعل إذا توقف التحميل بعد 70%؟ هل تحفظ raw data؟ كيف تتعامل مع تغير schema؟

## Project 02 — Warehouse + dbt + Airflow

**المستوى:** Intermediate. حوّل بيانات معاملات أو أحداث إلى raw/staging/marts. صمم star schema، عرّف grain لكل fact، طبّق surrogate keys وSCD Type 2 على dimension واحدة، ثم نسّق العملية عبر Airflow.

**المتطلبات:** dbt models وtests وdocs، freshness check، incremental model، backfill على تاريخ محدد، retries، alert، data quality report، وrunbook. افصل business transformations عن DAG code.

**أسئلة المقابلة التي يثبتها:** لماذا اخترت incremental؟ كيف تعرّف late-arriving data؟ ماذا يحدث عند إعادة تشغيل يوم سابق؟ كيف تختبر completeness وfreshness؟

## Project 03 — Streaming + Spark

**المستوى:** Advanced. أنشئ event producer، topic/partition strategy، consumer أو Spark Structured Streaming، ثم اكتب مخرجات Parquet أو table format. قارن النتيجة مع batch implementation.

**المتطلبات:** event-time windows، watermark، deduplication key، replay strategy، checkpoint، schema evolution note، metrics للـ lag والـ throughput، وbenchmark للـ partitioning أو join strategy.

**أسئلة المقابلة التي يثبتها:** هل الضمان at-least-once أم exactly-once؟ ماذا تفعل مع late events؟ كيف تعيد معالجة أسبوع؟ كيف تمنع small files؟

## Project 04 — Senior System Design Case

**المستوى:** Senior/Staff. صمّم منصة لبيانات clickstream أو marketplace orders لمستهلكين متعددين. اكتب requirements، estimates، architecture، data contracts، SLOs، security، cost، disaster recovery، وخطة migration.

**مخرجات إلزامية:** diagram Mermaid، ثلاثة ADRs، جدول trade-offs، incident playbook، وخمس دقائق narrative للمقابلة. يجب أن يحتوي التصميم على batch path حتى لو كان streaming هو الخيار الأساسي.

## Rubric موحد

| البعد | 0 | 1 | 2 |
|---|---|---|---|
| Correctness | لا يعمل | يعمل في المسار السعيد | يعالج edge cases ويدعم rerun |
| Quality | لا اختبارات | اختبارات أساسية | contract + freshness + regression |
| Operations | لا logs | logs يدوية | metrics/alerts/runbook |
| Design | أداة بلا سبب | سبب عام | trade-offs وأرقام وافتراضات |
| Communication | README ناقص | شرح التنفيذ | شرح المشكلة والقرار والبدائل |

## قالب README لكل مشروع

ابدأ بفقرة عن المشكلة والمستخدم، ثم أضف architecture diagram، dataset/source، assumptions، local setup، data model، pipeline flow، quality checks، failure modes، performance، cost، limitations، وما الذي ستبنيه لاحقاً. أرفق screenshots أو query outputs صغيرة فقط إذا كانت لا تحتوي على بيانات حساسة.
