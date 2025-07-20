#!/usr/bin/env python3
import sys
from typing import Self

import toml



from pydantic import AliasPath, BaseModel, Field, model_validator


class VersionData(BaseModel):
    version: str = Field(..., validation_alias=AliasPath("project", "version"))
    major: int = 0
    minor: int = 0
    patch: int = 0

    @property
    def new_version(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    @model_validator(mode="after")
    def set_version_variables(self) -> Self:
        major, minor, patch = self.version.split(".")
        self.major = int(major)
        self.minor = int(minor)
        self.patch = int(patch)
        return self

    def update_patch(self) -> None:
        self.patch += 1

    def update_minor(self) -> None:
        self.minor += 1
        self.patch = 0

    def update_major(self) -> None:
        self.major += 1
        self.minor = 0
        self.patch = 0


def main() -> None:
    with open("pyproject.toml") as file:
        pyproject_data = toml.load(file)
        version_data = VersionData(**pyproject_data)
    match sys.argv:
        case _, "patch":
            version_data.update_patch()
        case _, "minor":
            version_data.update_minor()
        case _, "major":
            version_data.update_major()
        case _:
            raise ValueError("Что-то не то...")

    pyproject_data["project"]["version"] = version_data.new_version
    with open("pyproject.toml", "w") as file:
        toml.dump(pyproject_data, file)
    print(f"Версия обновлена {version_data.version} -> {version_data.new_version}")


if __name__ == "__main__":
    main()
