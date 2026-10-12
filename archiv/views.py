from archiv.crud_registry import crud
from archiv.filters import (
    AutorListFilter,
    EventListFilter,
    KeyWordListFilter,
    OrtListFilter,
    SpatialCoverageListFilter,
    StelleListFilter,
    TextListFilter,
    UseCaseListFilter,
)
from archiv.models import (
    Autor,
    Event,
    KeyWord,
    Ort,
    SpatialCoverage,
    Stelle,
    Text,
    UseCase,
)

crud.register(
    Autor, filter_class=AutorListFilter, init_columns=["id", "name", "jahrhundert"]
)
crud.register(
    UseCase,
    filter_class=UseCaseListFilter,
    init_columns=["id", "title", "principal_investigator"],
    exclude_columns=["story_map"],
)
crud.register(KeyWord, filter_class=KeyWordListFilter, init_columns=["stichwort"])
crud.register(
    Ort, filter_class=OrtListFilter, init_columns=["id", "name", "name_antik"]
)
crud.register(
    Stelle,
    filter_class=StelleListFilter,
    init_columns=["id", "display_label", "text"],
)
crud.register(
    Text,
    filter_class=TextListFilter,
    init_columns=["id", "title", "not_before", "not_after"],
)
crud.register(
    Event,
    filter_class=EventListFilter,
    init_columns=["id", "title", "start_date", "end_date"],
)
crud.register(
    SpatialCoverage,
    filter_class=SpatialCoverageListFilter,
    init_columns=["id", "key_word", "fuzzyness"],
)
