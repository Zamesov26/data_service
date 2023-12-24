from dataaccess.utils.unitofwork import IUnitOfWork


class QuizService:
    @classmethod
    async def get_all(cls, uow: IUnitOfWork):
        async with uow:
            return await uow.questions.find_all()

    @classmethod
    async def get_all_with_answers(cls, uow: IUnitOfWork):
        async with uow:
            return await uow.questions.find_all_with_answer()

    @classmethod
    async def add_with_answer(cls, uow: IUnitOfWork, data):
        async with uow:
            question = await uow.questions.add_one(
                id=data['id'],
                text=data['text'],
                type=data['type'],
                img=data.get('img')
            )

            answers = []
            for answer_data in data.get('answers', []):
                answer = await uow.answers.add_one(**answer_data)
                answers.append(answer)
            question.answer = answers

            await uow.add(question)
            await uow.commit()

