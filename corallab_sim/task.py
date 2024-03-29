import sys
from .backend_manager import backend_manager


class Task:
    """A task bundles together an env and a robot from a particular
    backend.

    """

    def __init__(
            self,
            *args,
            env=None,
            robot=None,
            from_impl=None,
            backend=None,
            **kwargs
    ):
        TaskImpl = backend_manager.get_backend_attr(
            "TaskImpl",
            backend=backend
        )

        if from_impl:
            self.task_impl = TaskImpl.from_impl(
                from_impl,
                *args,
                **kwargs
            )
        else:
            self.task_impl = TaskImpl(
                *args,
                env=env.env_impl,
                robot=robot.robot_impl,
                **kwargs
            )

    def __getattr__(self, name):
        if hasattr(self.task_impl, name):
            return getattr(self.task_impl, name)
        else:
            # Default behaviour
            raise AttributeError
