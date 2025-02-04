from pydantic import BaseModel, Field


class RequestPaginationSchema(BaseModel):
    page: int = Field(
        0,
        description="Current page number",
        example=1
    )
    on_page: int = Field(
        10,
        description="Number of items per page",
        example=10
    )


class ResponsePaginationSchema(BaseModel):
    """
    Schema for paginated responses.
    """

    success: bool = Field(
        ...,
        description="Indicates if the request was successful",
        example=True
    )
    total: int = Field(
        ...,
        description="Total number of items",
        example=100
    )
    page: int = Field(
        ...,
        description="Current page number",
        example=1
    )
    on_page: int = Field(
        ...,
        description="Number of items per page",
        example=10
    )
    next_page: int | None = Field(
        None,
        description="Next page number (None if last page)",
        example=2
    )




