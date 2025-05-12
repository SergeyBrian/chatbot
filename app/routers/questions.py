from fastapi import APIRouter, File, UploadFile
from app.db.questions.usecases import Usecases, SelectInput
from app.db.questions.pg import Repo
from app.utils import safe_execute, ResponseModel
from app.model.question import Question
from app.model.question_csv import QuestionCSV
from io import StringIO
from fastapi.responses import StreamingResponse
import csv

router = APIRouter(prefix='/questions', tags=["questions"])

repo = Repo()
uc = Usecases(repo)


@router.get('/', response_model=ResponseModel[list[Question]])
def get_questions(
        limit: int = 7,
        offset: int = 0,
        category_id: int = 0,
        search: str = ""):
    return safe_execute(uc.get, SelectInput(
        limit=limit,
        offset=offset,
        search=search,
    ))


@router.post('/', response_model=ResponseModel[Question])
def create_question(question: Question):
    return safe_execute(uc.create, question)


@router.delete('/{id}', response_model=ResponseModel[int])
def delete_question(id: int):
    return safe_execute(uc.delete, id)


@router.post('/import', response_model=ResponseModel[int])
async def import_questions(file: UploadFile = File(...)):
    content = await file.read()
    csv_text = content.decode('utf-8')
    reader = csv.DictReader(StringIO(csv_text))
    questions = [QuestionCSV(**row) for row in reader]
    return safe_execute(uc.import_from_csv, questions)


@router.get('/export', response_model=None)
def export_questions():
    questions = uc.get_all_for_export()
    output = StringIO()
    writer = csv.DictWriter(
        output, fieldnames=["category", "question", "answer"])
    writer.writeheader()
    for q in questions:
        writer.writerow(q.dict())
    output.seek(0)
    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=questions.csv"}
    )
