from archiv.crud_registry import crud
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

crud.register(Autor, init_columns=["id", "name", "jahrhundert"])
crud.register(
    UseCase,
    init_columns=["id", "title", "principal_investigator"],
    exclude_columns=["story_map"],
)
crud.register(KeyWord, init_columns=["stichwort"])
crud.register(Ort, init_columns=["id", "name", "name_antik"])
crud.register(Stelle, init_columns=["id", "display_label", "text"])
crud.register(Text, init_columns=["id", "title", "not_before", "not_after"])
crud.register(Event, init_columns=["id", "title", "start_date", "end_date"])
crud.register(SpatialCoverage, init_columns=["id", "key_word", "fuzzyness"])
