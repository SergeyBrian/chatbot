from yoyo import step

steps = [
    step("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            session_id TEXT UNIQUE,
            username TEXT,
            created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );
    """),
    step("""
        CREATE TABLE IF NOT EXISTS dialogs (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            status TEXT NOT NULL
                CHECK (status IN ('new','in_progress','closed')) DEFAULT 'new',
            started_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            closed_at TIMESTAMP WITHOUT TIME ZONE
        );
    """),
    step("""
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            dialog_id INTEGER NOT NULL REFERENCES dialogs(id) ON DELETE CASCADE,
            sender TEXT NOT NULL
                CHECK (sender IN ('user','bot','operator')),
            content TEXT NOT NULL,
            created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );
    """),
    step("""
        CREATE TABLE IF NOT EXISTS knowledge_base (
            id SERIAL PRIMARY KEY,
            category TEXT NOT NULL,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            variations JSONB DEFAULT '[]'::jsonb
        );
    """),
    step("""
        CREATE TABLE IF NOT EXISTS feedback (
            id SERIAL PRIMARY KEY,
            message_id INTEGER NOT NULL REFERENCES messages(id) ON DELETE CASCADE,
            is_useful BOOLEAN NOT NULL,
            comment TEXT
        );
    """),
    step("""
        CREATE TABLE IF NOT EXISTS operators (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL
                CHECK (role IN ('admin','operator')) DEFAULT 'operator'
        );
    """),
]
