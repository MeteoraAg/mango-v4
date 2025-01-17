use anchor_lang::prelude::*;

use crate::state::*;

#[derive(Accounts)]
#[instruction(market_index: Serum3MarketIndex)]
pub struct Serum3EditMarket<'info> {
    #[account(
        has_one = admin,
        constraint = group.load()?.serum3_supported()
    )]
    pub group: AccountLoader<'info, Group>,
    pub admin: Signer<'info>,

    #[account(
        mut,
        has_one = group
    )]
    pub market: AccountLoader<'info, Serum3Market>,
}
