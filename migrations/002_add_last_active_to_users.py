from yoyo import step

steps = [
    step("""
        ALTER TABLE users
        ADD COLUMN IF NOT EXISTS last_active TIMESTAMP WITHOUT TIME ZONE
            DEFAULT CURRENT_TIMESTAMP;
    """)
]
