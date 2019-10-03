class Tile:
    """
    A tile on a map. It may or may not be blocked or block sight
    """
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        # By default a blocked tile also blocks sight
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight