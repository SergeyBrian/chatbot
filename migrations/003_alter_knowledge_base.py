from yoyo import step

steps = [
    step("""
        ALTER TABLE knowledge_base
        ADD COLUMN IF NOT EXISTS related_questions JSONB DEFAULT '[]'::jsonb;
    """),
    step("""
        ALTER TABLE knowledge_base
        ADD COLUMN IF NOT EXISTS hints JSONB DEFAULT '[]'::jsonb;
    """),
]
