# خارطة الطريق التفصيلية

## قبل البداية: ما الذي يفعله Data Engineer؟

المهندس يحول مصادر غير مستقرة إلى بيانات يمكن الوثوق بها واستخدامها. لذلك فإن النجاح لا يعني معرفة Spark أو Cloud فقط؛ بل فهم **الصحة (correctness)**، والاعتمادية، والأمان، والتكلفة، وتجربة المستخدم الداخلي الذي سيستهلك البيانات.

## المستوى 0 — Foundations

**الهدف:** امتلاك أساس برمجي وبياني يكفي لفهم كل ما يأتي بعده.

| محور | ما يجب تعلمه | معيار الإتقان |
|---|---|---|
| Linux وCLI | files, pipes, grep, curl, permissions, processes, environment variables | تشغيل مشروع كامل من terminal وقراءة logs |
| Git | branches، commits، pull requests، conflict resolution، README | history نظيف وPR صغير موثق |
| Python | functions، modules، exceptions، iterators/generators، typing، logging، JSON/CSV، virtual environments | برنامج قابل للاختبار يعالج ملفات كبيرة دون تحميلها كلها |
| SQL | SELECT، joins، aggregations، CTEs، window functions، NULL، dates، indexes | حل مسائل business مع شرح grain وedge cases |
| قواعد البيانات | primary/foreign keys، normalization، transactions، isolation، EXPLAIN | تصميم schema وشرح سبب كل constraint |
| HTTP والبيانات | REST، pagination، retries، status codes، JSON، rate limits | عميل API يتحمل الفشل ويكتب raw snapshots |

**مشروع الإثبات:** برنامج يسحب بيانات عامة من API مع pagination وretry، يخزن raw JSON، ينظفها، ويكتبها إلى PostgreSQL. أضف اختبارات لوظائف التحويل وREADME يشرح حالات الفشل.

## المستوى 1 — Junior-ready

**الهدف:** تنفيذ Batch pipeline صغيرة end-to-end دون فقدان البيانات أو تكرارها عند إعادة التشغيل.

| محور | ما يجب تعلمه | تطبيق عملي |
|---|---|---|
| Ingestion | full load، incremental load، watermark، checkpoint، schema validation | تحميل يومي مع `updated_at` |
| Modeling | grain، facts/dimensions، star schema، surrogate keys، slowly changing dimensions | نموذج طلبات/عملاء قابل للتحليل |
| Docker | images، containers، volumes، networks، Compose | تشغيل PostgreSQL وpipeline بأمر واحد |
| Quality | unit/integration tests، null/unique/range checks، data contracts | فشل واضح عند وصول schema غير متوقع |
| Engineering | configuration، secrets، logging، retries، idempotency | تشغيل ثانٍ لا يكرر السجلات |

**مشروع الإثبات:** `projects/01-batch-api-to-postgres`. لا يكفي أن ينجح مرة؛ يجب أن تبرهن أن rerun وpartial failure وduplicate input حالات آمنة.

## المستوى 2 — Production-ready

**الهدف:** بناء طبقة تحليلية قابلة للصيانة والتشغيل بواسطة فريق.

تعلم الفرق بين raw، staging، intermediate، وmart layers، ثم طبّق transformations modular عبر dbt أو SQL واضح. أضف lineage، documentation، tests، incremental models، partition strategy، وfreshness SLA. استخدم Airflow لتنسيق المهام، مع فصل orchestration عن business logic حتى يمكن اختبار المنطق خارج الـ DAG.

**مشروع الإثبات:** `projects/02-warehouse-dbt-airflow`. يجب أن يضم warehouse محلياً، models موثقة، tests، DAG، backfill، alert عند الفشل، وrunbook قصيراً للمناوب.

## المستوى 3 — Advanced

**الهدف:** فهم ما يتغير عندما تصبح البيانات كبيرة أو سريعة أو موزعة.

| محور | مفاهيم لا بد من شرحها |
|---|---|
| Spark | partitions، shuffles، joins، caching، lazy evaluation، narrow/wide transformations، skew، AQE |
| File formats | Parquet، compression، column pruning، partition pruning، small files |
| Streaming | event time vs processing time، windows، watermark، late events، offsets، delivery semantics |
| Kafka | topics، partitions، consumer groups، ordering، retention، replay، schema registry concept |
| Lakehouse | table format، ACID، compaction، schema evolution، medallion layers |
| Performance | throughput، latency، backpressure، cost per run، cluster sizing |

**مشروع الإثبات:** `projects/03-streaming-spark-pipeline`. نفّذ replay وdeduplication، اختبر late data، وقارن batch وstreaming بجدول trade-offs.

## المستوى 4 — Senior/Staff

**الهدف:** تصميم منصة تحقق متطلبات العمل وتظل قابلة للتشغيل عند التوسع.

في هذا المستوى لا توجد إجابة أداة واحدة صحيحة. ابدأ بالمتطلبات: حجم البيانات، معدل الوصول، freshness، retention، privacy، recovery point/time objectives، وعدد المستهلكين. بعد ذلك قارن lake/warehouse/lakehouse، batch/stream، managed/self-hosted، ثم احسب تقريباً throughput والتكلفة وحدد failure modes.

المخرجات المطلوبة هي architecture diagram، ADRs، data contracts، SLOs، incident playbook، security model، cost model، وخطة migration. تدرب على شرح trade-off بصوت عالٍ خلال 30–45 دقيقة.

## ترتيب لا ينبغي كسره

لا تبدأ بـ Kubernetes أو streaming قبل إتقان SQL وdata modeling وidempotent batch. ولا تبدأ بتعدد السحابات قبل فهم storage، compute، orchestration، networking، وIAM كمفاهيم مجردة. اختر Cloud واحدة للمشروع، ثم انقل المفاهيم إلى AWS/GCP/Azure في مرحلة المراجعة.

## Definition of Done لكل مستوى

لا يعتبر المستوى منتهياً بمجرد مشاهدة دورة. يكون منتهياً عندما تستطيع شرح الفكرة، كتابة تنفيذ صغير، إضافة اختبار، التعامل مع failure، وكتابة README يستطيع شخص آخر تشغيله. استخدم معياراً من خمس درجات: **فهم، تنفيذ، اختبار، تشغيل، شرح مقابلة**؛ ولا تنتقل إذا كانت درجة التنفيذ أو الشرح أقل من 3/5.

## References

[1]: https://roadmap.sh/data-engineer "roadmap.sh — Data Engineer Roadmap"
[2]: https://github.com/DataTalksClub/data-engineering-zoomcamp "DataTalksClub — Data Engineering Zoomcamp"
[3]: https://spark.apache.org/ "Apache Spark official website"
[4]: https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html "Apache Airflow Tutorials"
[5]: https://docs.getdbt.com/docs/get-started-dbt "dbt Quickstarts"
