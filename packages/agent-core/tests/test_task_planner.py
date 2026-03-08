from planner import TaskPlanner


def test_task_planner_generates_house_plan() -> None:
    planner = TaskPlanner()
    planned = planner.plan("建个小屋然后添加材质")

    assert len(planned.steps) >= 2
    assert planned.steps[0].calls[0].name == "create_primitive"
    assert planned.steps[1].calls[0].name in {"set_material", "run_nl_action"}


def test_task_planner_rebuild_after_failure() -> None:
    planner = TaskPlanner(max_retry=2)
    planned = planner.plan("移动选中物体")
    rebuilt = planner.rebuild_after_failure(planned, failed_step_index=1, error="tool timeout")

    assert rebuilt.metadata["replanned_step"] == 1
    assert rebuilt.steps[0].calls[0].retry == 1
