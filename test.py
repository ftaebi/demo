from classes import typeclass
from dataclasses import dataclass


@dataclass
class SourceA:
    pass


@dataclass
class SourceB:
    pass


@typeclass
def find_by(instance) -> str:
    ...


@find_by.instance(SourceA)
def _find_by_source_a(instance: SourceA) -> str:
    return "source_a"


@find_by.instance(SourceB)
def _find_by_source_b(instance: SourceB) -> str:
    return "source_b"
