from yoyo import step

steps = [
    step("""
        CREATE TABLE IF NOT EXISTS unanswered_questions (
            id SERIAL PRIMARY KEY,
            dialog_id INTEGER REFERENCES dialogs(id) ON DELETE SET NULL,
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            question_text TEXT NOT NULL,
            created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            processed BOOLEAN NOT NULL DEFAULT FALSE
        );
    """)
]
