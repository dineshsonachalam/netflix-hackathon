describe("Search kings", () => {
    it('Load search page', () => {
        cy.visit("http://localhost:3000")
    })
    it('Select king', () => {
        cy.get('.ant-select-selector').type('joffrey').type('{enter}')
        cy.wait(5000)
    })

    it('Compare kings ranking', () => {
        cy.wait(10000)
        let expected_kings_data = [
            {
                "key": 3,
                "king": "Balon/Euron Greyjoy",
                "rating": 1031.9923,
                "wins": 4,
                "loss": 1,
                "battles": 5,
                "rank": 1
            },
            {
                "key": 4,
                "king": "Stannis Baratheon",
                "rating": 997.80141,
                "wins": 1,
                "loss": 1,
                "battles": 2,
                "rank": 2
            },
            {
                "key": 2,
                "king": "Robb Stark",
                "rating": 997.36995,
                "wins": 8,
                "loss": 11,
                "battles": 19,
                "rank": 3
            },
            {
                "key": 1,
                "king": "Joffrey/Tommen Baratheon",
                "rating": 988.83634,
                "wins": 8,
                "loss": 7,
                "battles": 15,
                "rank": 4
            },
            {
                "key": 5,
                "king": "Renly Baratheon",
                "rating": 984.0,
                "wins": 0,
                "loss": 1,
                "battles": 1,
                "rank": 5
            }
        ];
        for (var index=0; index < expected_kings_data.length; index++) {   
            const index_pos = index;
            let table_key = expected_kings_data[index_pos]["key"];
            cy.get(`:nth-child(5) > .site-page-header-ghost-wrapper > .ant-page-header > .ant-page-header-content > .ant-table-wrapper > .ant-spin-nested-loading > .ant-spin-container > .ant-table > .ant-table-container > .ant-table-content > table > .ant-table-tbody > [data-row-key=${table_key}] > :nth-child(1)`).then(($rank_elem) => {
                let rank = $rank_elem.text();
                let expected_rank =  expected_kings_data[index_pos]["rank"].toString();
                expect(rank).to.deep.eq(expected_rank);
            })
            cy.get(`:nth-child(5) > .site-page-header-ghost-wrapper > .ant-page-header > .ant-page-header-content > .ant-table-wrapper > .ant-spin-nested-loading > .ant-spin-container > .ant-table > .ant-table-container > .ant-table-content > table > .ant-table-tbody > [data-row-key=${table_key}] > :nth-child(2)`).then(($king_elem) => {
                let king = $king_elem.text();
                let expected_king =  expected_kings_data[index_pos]["king"];
                expect(king).to.deep.eq(expected_king);
            })
            cy.get(`:nth-child(5) > .site-page-header-ghost-wrapper > .ant-page-header > .ant-page-header-content > .ant-table-wrapper > .ant-spin-nested-loading > .ant-spin-container > .ant-table > .ant-table-container > .ant-table-content > table > .ant-table-tbody > [data-row-key=${table_key}] > :nth-child(3)`).then(($rating_elem) => {
                let rating = $rating_elem.text();
                let expected_rating =  expected_kings_data[index_pos]["rating"].toString();
                expect(rating).to.deep.eq(expected_rating);
            })
            cy.get(`:nth-child(5) > .site-page-header-ghost-wrapper > .ant-page-header > .ant-page-header-content > .ant-table-wrapper > .ant-spin-nested-loading > .ant-spin-container > .ant-table > .ant-table-container > .ant-table-content > table > .ant-table-tbody > [data-row-key=${table_key}] > :nth-child(4)`).then(($wins_elem) => {
                let wins = $wins_elem.text();
                let expected_wins =  expected_kings_data[index_pos]["wins"].toString();
                expect(wins).to.deep.eq(expected_wins);
            })
            cy.get(`:nth-child(5) > .site-page-header-ghost-wrapper > .ant-page-header > .ant-page-header-content > .ant-table-wrapper > .ant-spin-nested-loading > .ant-spin-container > .ant-table > .ant-table-container > .ant-table-content > table > .ant-table-tbody > [data-row-key=${table_key}] > :nth-child(5)`).then(($loss_elem) => {
                let loss = $loss_elem.text();
                let expected_loss =  expected_kings_data[index_pos]["loss"].toString();
                expect(loss).to.deep.eq(expected_loss);
            })
            cy.get(`[data-row-key=${table_key}] > :nth-child(6)`).then(($battles_elem) => {
                let battles = $battles_elem.text();
                let expected_battles =  expected_kings_data[index_pos]["battles"].toString();
                expect(battles).to.deep.eq(expected_battles);
            })
        }
    })
})
