from pathlib import Path

from router import ToolRouter
from skills import SkillExecutor, SkillMetadata, SkillRecord, SkillStep, SkillStore


def test_skill_store_save_and_load(tmp_path: Path) -> None:
    store = SkillStore(tmp_path)
    skill = SkillRecord(
        skill_id="create_cube",
        metadata=SkillMetadata(name="Create Cube", description="Create a cube object"),
        capsule=[SkillStep(tool_name="create_primitive", arguments={"type": "cube"})],
    )

    saved_path = store.save(skill)
    loaded = store.load("create_cube")

    assert saved_path.exists()
    assert loaded is not None
    assert loaded.metadata.name == "Create Cube"


def test_skill_executor_runs_registered_tool() -> None:
    router = ToolRouter()

    def create_primitive(arguments: dict[str, object]) -> dict[str, object]:
        return {
            "ok": True,
            "created": arguments.get("name", "unnamed"),
            "object_count": 1,
        }

    router.register_tool("create_primitive", create_primitive, required_args=("name",))
    executor = SkillExecutor(router)

    skill = SkillRecord(
        skill_id="create_cube",
        metadata=SkillMetadata(name="Create Cube", description="Create cube"),
        capsule=[
            SkillStep(
                tool_name="create_primitive",
                arguments={"name": "${object_name}"},
                validation={"object_count": 1},
            )
        ],
    )

    result = executor.execute(skill, variables={"object_name": "Cube"})

    assert result.ok is True
    assert result.step_results[0].response["created"] == "Cube"
