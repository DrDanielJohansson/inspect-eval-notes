from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import model_graded_qa
from inspect_ai.solver import generate
from inspect_ai.model import ModelOutput, get_model

@task
def forced_grade():
    grader = get_model(
    "mockllm/model",
    custom_outputs=[
        ModelOutput.from_content(
            model="mockllm/model",
            content="The answer matches the target. GRADE: CI",#Correct, CORRECT, C, c
        )
    ],
)
    return Task(
        dataset=[Sample(input="Say hello", target="hello")],
        solver=generate(),
        scorer=model_graded_qa(
            model=grader#,
            #grade_pattern=r"(?is).*(?<!\w)GRADE(?!\w)\s*:\s*(Correct|Partial|Incorrect|[CPI])(?!\w)",
        ),
    )
