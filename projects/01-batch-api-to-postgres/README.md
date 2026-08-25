# Project 01 — Batch API to PostgreSQL

هذا starter صغير للمستوى Junior. يبدأ بتحويل records خام إلى records قابلة للتحميل، مع إزالة التكرار بطريقة deterministic. وسّعه لاحقاً بإضافة API client وPostgreSQL وDocker.

## الهدف

تعلم فصل ingestion عن transformation، وإثبات أن إعادة تشغيل نفس الدفعة لا تضيف صفوفاً مكررة. في النسخة الكاملة يجب حفظ raw payload قبل التحويل، ثم تحميل staging، ثم تنفيذ upsert أو merge على business key.

## التشغيل

```bash
python -m pytest
```

الكود الحالي لا يحتاج مكتبات خارجية؛ أضف dependencies فقط عند بناء النسخة الكاملة. الأسئلة المطلوبة في README النهائي: ما هو business key؟ ماذا يحدث عند وصول record أقدم؟ كيف تراقب عدد records المستلمة والمرفوضة؟

## التوسعة المقترحة

أضف `extract.py` مع pagination وretry، و`load.py` مع PostgreSQL transaction، وDocker Compose، ثم integration test. لا تضع API keys في Git؛ استخدم `.env.example` فقط.
