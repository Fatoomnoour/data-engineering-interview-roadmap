# Data Engineering Interview Prep

المقابلة تقيس قدرتك على التفكير في بيانات ناقصة وفشل حقيقي، لا قدرتك على ترديد تعريفات. في كل إجابة ابدأ بالافتراضات، ثم اشرح الحل، ثم اختبره، ثم ناقش trade-offs والتشغيل.

## SQL screen

تدرّب على joins، aggregations، CTEs، window functions، deduplication، gaps-and-islands، dates، NULL semantics، وquery optimization. قبل كتابة SQL اسأل: ما هو grain؟ هل الصفوف قد تتكرر؟ ما النتيجة المطلوبة عند عدم وجود match؟

**قالب الإجابة:** اشرح الجداول والمفتاح، اكتب حلًا واضحاً، اختبره على duplicate وNULL وempty input، ثم اذكر التعقيد والفهارس أو partitioning المناسب.

## Python/coding

المطلوب غالباً كود مقروء يعالج collections أو ملفات أو batches. اذكر complexity، memory pressure، streaming/generator approach، validation، exceptions، typing، tests، وlogging. لا تبالغ في abstraction؛ اجعل الكود قابلاً للتشغيل والاختبار.

## Data modeling

ابدأ بالـ grain قبل الأعمدة. فرّق بين natural وsurrogate keys، وحدد cardinality والقيود. قارن normalization للأنظمة التشغيلية مع dimensional modeling للتحليلات. عند SCD اشرح ما الذي يجب أن يراه المستهلك عند تغير attribute ومتى يصبح history غير صحيح.

## Pipeline/system design

استخدم هذا التسلسل في كل prompt: **Clarify → Estimate → Freshness → Batch/Stream → Storage → Topology → Failure modes → Cost/Operations**. اذكر source، ingestion، raw retention، transforms، serving، consumers، schema contract، idempotency، retries، backfill، deduplication، observability، security، وownership.

## أسئلة تدريبية

| المحور | Prompt |
|---|---|
| SQL | احسب أعلى ثلاثة منتجات في كل بلد شهرياً مع معالجة التعادل |
| SQL | اكتشف المستخدمين النشطين 7 أيام متتالية دون تكرار الأحداث |
| Python | اكتب batch processor يعيد المحاولة ولا يكرر الملفات التي عولجت |
| Modeling | صمم schema لتاريخ أسعار المنتج مع صلاحية زمنية |
| Batch | صمم ingestion يومي لمصدر API يتأخر أحياناً |
| Streaming | صمم عداداً لحظياً مع late events وreplay |
| Reliability | كيف تعيد بناء partition فاسدة دون كسر downstream؟ |
| Cost | كيف تخفض تكلفة query-heavy warehouse مع الحفاظ على freshness؟ |

## Behavioral

حضّر ست قصص STAR من مشاريعك: مشكلة غامضة امتلكتها من البداية، اختلاف مع stakeholder، incident في الإنتاج، تحسين أو mentoring، قرار بإيقاف عمل غير مفيد، وتسليم سريع أعقبه cleanup. اجعل لكل قصة سياقاً مختصراً، تصرفات محددة، نتيجة قابلة للقياس، ودرساً.

## تقييم mock interview

بعد كل مقابلة سجّل هل عرّفت الافتراضات، هل شرحت grain، هل ذكرت failure modes، هل دعمت الاختيار بأرقام، وهل حافظت على وضوح الكلام. أعد نفس السؤال بعد 48 ساعة، ولا تحفظ صياغة الإجابة حرفياً.

## مراجع ممارسة

استفد من [Data Engineering Interview Handbook](https://github.com/datadriven-io/data-engineering-interview-handbook) لمحاور التدريب وأمثلة study plans، ثم نفّذ الحلول بنفسك في ملفاتك. استخدم [LeetCode SQL](https://leetcode.com/studyplan/top-sql-50/) أو [SQLBolt](https://sqlbolt.com/) للتكرار، لكن اربط كل مسألة بمشكلة data pipeline أو business حقيقية.
