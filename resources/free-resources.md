# مصادر مجانية موثوقة

اختر مصدراً أساسياً واحداً لكل محور، ثم استخدم مصادر إضافية لسد فجوة محددة. كثرة الروابط ليست تقدماً؛ التقدم هو تنفيذ ما قرأته وكتابة ملاحظاتك واختباراتك.

| المحور | المصدر | كيف تستخدمه |
|---|---|---|
| خارطة عامة | [roadmap.sh Data Engineer](https://roadmap.sh/data-engineer) | راجع التسلسل العام واستخدمه لاكتشاف الفجوات، لا كخطة تنفيذ وحيدة. |
| Python | [Python Tutorial](https://docs.python.org/3/tutorial/) | الأساسيات، modules، exceptions، iterators، generators، files، virtual environments. |
| SQL/PostgreSQL | [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html) | SQL العلائقي وPostgreSQL بشكل عملي، ثم انتقل إلى EXPLAIN والفهارس من التوثيق الكامل. |
| SQL practice | [SQLBolt](https://sqlbolt.com/) و[LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/) | تدريب يومي مع كتابة شرح للحل والـ edge cases. |
| مشروع end-to-end | [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) | منهج مجاني project-based؛ استخدم وحداته كخطة مشاريع، مع قراءة الإصدارات الحالية قبل التنفيذ. |
| Orchestration | [Apache Airflow Tutorials](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html) | ابدأ بـ Airflow 101 وTaskFlow وSimple Data Pipeline، ثم أضف retries وbackfills. |
| Analytics engineering | [dbt Quickstarts](https://docs.getdbt.com/docs/get-started-dbt) و[dbt Learn](https://learn.getdbt.com/) | models، tests، docs، incremental transformations، واختيار local DuckDB أو warehouse. |
| Distributed processing | [Apache Spark](https://spark.apache.org/) و[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) | PySpark، SQL، batch/streaming، partitions، joins، وقياس الأداء. |
| Streaming | [Apache Kafka Documentation](https://kafka.apache.org/documentation/) | topics، partitions، consumer groups، offsets، retention، وdelivery semantics. |
| Containers | [Docker Get Started](https://docs.docker.com/get-started/) | images، containers، Compose، volumes، networks، reproducible local setup. |
| Data modeling | [Kimball Group Techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/) | grain، facts/dimensions، dimensional modeling، وSCD terminology. |
| Interview structure | [Data Engineering Interview Handbook](https://github.com/datadriven-io/data-engineering-interview-handbook) | محاور SQL/Python/modeling/pipeline/system design/behavioral؛ استعمله للتمرين لا للنسخ. |
| System design practice | [System Design for Data Engineers](https://github.com/datadriven-io/system-design-for-data-engineers) | prompts متعددة؛ أجب بقالب assumptions → estimates → trade-offs → failure modes. |

## لماذا هذه المصادر؟

المصادر الرسمية هي المرجع الأول لتعريف الأداة وسلوكها. Python يوضح أن الـ tutorial يغطي أساسيات اللغة والملفات والاستثناءات والـ generators والبيئات؛ PostgreSQL يقدّم مقدمة عملية للـ relational concepts وSQL؛ Airflow يضم tutorials لبناء workflows وdata pipelines؛ وdbt يوفّر quickstarts لكل من التطوير المحلي والمنصة. أما Spark فيعرّف نفسه كمحرك متعدد اللغات للـ batch والـ streaming والمعالجة واسعة النطاق. هذه الأوصاف موثقة في الروابط الأصلية وليست ملخصات تسويقية منقولة.

## قواعد استخدام المصادر

تحقق من تاريخ التوثيق عند بدء المشروع، وثبّت version في README، ولا تضع secrets أو بيانات شخصية في notebooks. عند استخدام مادة من repository خارجي، راجع LICENSE واذكر الرابط والمؤلف. اجعل كل رابط داخل هذا الملف قابلاً للتصفح، واستبدل الرابط إذا أصبح مكسوراً.

## References

[1]: https://docs.python.org/3/tutorial/ "Python Tutorial"
[2]: https://www.postgresql.org/docs/current/tutorial.html "PostgreSQL Tutorial"
[3]: https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html "Apache Airflow Tutorials"
[4]: https://docs.getdbt.com/docs/get-started-dbt "dbt Quickstarts"
[5]: https://spark.apache.org/ "Apache Spark official website"
[6]: https://github.com/DataTalksClub/data-engineering-zoomcamp "Data Engineering Zoomcamp"
[7]: https://github.com/datadriven-io/data-engineering-interview-handbook "Data Engineering Interview Handbook"
