from .elements import ClauseElement
from .base import Executable, SchemaVisitor

class _DDLCompiles(ClauseElement): ...
class DDLElement(Executable, _DDLCompiles): ...
class DDL(DDLElement): ...
class _CreateDropBase(DDLElement): ...
class CreateSchema(_CreateDropBase): ...
class DropSchema(_CreateDropBase): ...
class CreateTable(_CreateDropBase): ...
class _DropView(_CreateDropBase): ...
class CreateColumn(_DDLCompiles): ...
class DropTable(_CreateDropBase): ...
class CreateSequence(_CreateDropBase): ...
class DropSequence(_CreateDropBase): ...
class CreateIndex(_CreateDropBase): ...
class DropIndex(_CreateDropBase): ...
class AddConstraint(_CreateDropBase): ...
class DropConstraint(_CreateDropBase): ...
class DDLBase(SchemaVisitor): ...
class SchemaGenerator(DDLBase): ...
class SchemaDropper(DDLBase): ...

def sort_tables(tables, skip_fn=..., extra_dependencies=...): ...
def sort_tables_and_constraints(tables, filter_fn=..., extra_dependencies=...): ...