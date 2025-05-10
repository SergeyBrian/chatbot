from yoyo import step

steps = [
    step("""
        ALTER TABLE messages
        ADD COLUMN IF NOT EXISTS useful BOOL;
    """),
    step("""
        DROP TABLE feedback;
    """),
]
