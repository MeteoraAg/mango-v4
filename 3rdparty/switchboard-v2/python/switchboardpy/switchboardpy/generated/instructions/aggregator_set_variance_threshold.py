from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class AggregatorSetVarianceThresholdArgs(typing.TypedDict):
    params: types.aggregator_set_variance_threshold_params.AggregatorSetVarianceThresholdParams


layout = borsh.CStruct(
    "params"
    / types.aggregator_set_variance_threshold_params.AggregatorSetVarianceThresholdParams.layout
)


class AggregatorSetVarianceThresholdAccounts(typing.TypedDict):
    aggregator: PublicKey
    authority: PublicKey


def aggregator_set_variance_threshold(
    args: AggregatorSetVarianceThresholdArgs,
    accounts: AggregatorSetVarianceThresholdAccounts,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["aggregator"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["authority"], is_signer=True, is_writable=False),
    ]
    identifier = b"\xd4)\xee\xe7w}\x96\x06"
    encoded_args = layout.build(
        {
            "params": args["params"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, PROGRAM_ID, data)
