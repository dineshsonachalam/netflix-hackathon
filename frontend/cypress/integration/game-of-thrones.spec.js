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

        let expected_kings_data = {
            1: {
                "key": 3,
                "king": "Balon/Euron Greyjoy",
                "rating": 1049.86133,
                "wins": 12,
                "loss": 6,
                "battles": 18,
                "rank": 1
            },
            2: {
                "key": 1,
                "king": "Joffrey/Tommen Baratheon",
                "rating": 1042.30656,
                "wins": 32,
                "loss": 22,
                "battles": 54,
                "rank": 2
            }
        }
        let total_kings = Object.keys(expected_kings_data).length
        
        for (var index=1; index < total_kings+1; index++) {   
            let table_key = expected_kings_data[index]["key"]
            let expected_rank =  expected_kings_data[index]["rank"].toString();
            let expected_king =  expected_kings_data[index]["king"];
            let expected_rating =  expected_kings_data[index]["rating"].toString();
            let expected_wins =  expected_kings_data[index]["wins"].toString();
            let expected_loss =  expected_kings_data[index]["loss"].toString();
            let expected_battles =  expected_kings_data[index]["battles"].toString();

            cy.get(`:nth-child(5) > .site-page-header-ghost-wrapper > .ant-page-header > .ant-page-header-content > .ant-table-wrapper > .ant-spin-nested-loading > .ant-spin-container > .ant-table > .ant-table-container > .ant-table-content > table > .ant-table-tbody > [data-row-key=${table_key}] > :nth-child(1)`).then(($rank_elem) => {
                let rank = $rank_elem.text();
                console.log("Rank: ", rank)
                console.log("Expected Rank: ", expected_rank)
                console.log("expected_king: ", expected_king)
                expect(rank).to.deep.eq(expected_rank);
            })
            cy.get(`:nth-child(5) > .site-page-header-ghost-wrapper > .ant-page-header > .ant-page-header-content > .ant-table-wrapper > .ant-spin-nested-loading > .ant-spin-container > .ant-table > .ant-table-container > .ant-table-content > table > .ant-table-tbody > [data-row-key=${table_key}] > :nth-child(2)`).then(($king_elem) => {
                let king = $king_elem.text();
                expect(king).to.deep.eq(expected_king);
            })
            cy.get(`:nth-child(5) > .site-page-header-ghost-wrapper > .ant-page-header > .ant-page-header-content > .ant-table-wrapper > .ant-spin-nested-loading > .ant-spin-container > .ant-table > .ant-table-container > .ant-table-content > table > .ant-table-tbody > [data-row-key=${table_key}] > :nth-child(3)`).then(($rating_elem) => {
                let rating = $rating_elem.text();
                expect(rating).to.deep.eq(expected_rating);
            })
            cy.get(`:nth-child(5) > .site-page-header-ghost-wrapper > .ant-page-header > .ant-page-header-content > .ant-table-wrapper > .ant-spin-nested-loading > .ant-spin-container > .ant-table > .ant-table-container > .ant-table-content > table > .ant-table-tbody > [data-row-key=${table_key}] > :nth-child(4)`).then(($wins_elem) => {
                let wins = $wins_elem.text();
                expect(wins).to.deep.eq(expected_wins);
            })
            cy.get(`:nth-child(5) > .site-page-header-ghost-wrapper > .ant-page-header > .ant-page-header-content > .ant-table-wrapper > .ant-spin-nested-loading > .ant-spin-container > .ant-table > .ant-table-container > .ant-table-content > table > .ant-table-tbody > [data-row-key=${table_key}] > :nth-child(5)`).then(($loss_elem) => {
                let loss = $loss_elem.text();
                expect(loss).to.deep.eq(expected_loss);
            })
            cy.get(`[data-row-key=${table_key}] > :nth-child(6)`).then(($battles_elem) => {
                let battles = $battles_elem.text();
                expect(battles).to.deep.eq(expected_battles);
            })
        }
    })
})
