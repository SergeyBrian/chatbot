from yoyo import step

steps = [
    step("""
        CREATE TABLE IF NOT EXISTS analytics (
            id SERIAL PRIMARY KEY,
            report_date DATE UNIQUE NOT NULL,
            processed_requests INTEGER NOT NULL DEFAULT 0,
            success_rate NUMERIC(5,2) NOT NULL DEFAULT 0.0,
            operator_requests INTEGER NOT NULL DEFAULT 0,
            top_questions JSONB DEFAULT '[]'::jsonb
        );
    """)
]
