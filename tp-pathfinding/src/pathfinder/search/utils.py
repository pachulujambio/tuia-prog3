from ..models.grid import Grid

def get_start_value(grid: Grid) -> str:
    """
    Return start value of the first node.

    -- Deprecated function --
    """
    return grid.get_node(grid.start).value