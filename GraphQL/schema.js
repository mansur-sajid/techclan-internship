export const typeDefs = `#graphql
type Game{
    id: ID!
    title: String!
    platform: [String!]!
    reviews : [Review]
    
}

type Review{
    id: ID!
    rating: Int!
    content: String!
    authors: [Author]
    game : Game
}

type Author{
    id: ID!
    name: String!
    verified: Boolean!
}

type Query{
    reviews: [Review]
    review(id: ID!): Review
    games: [Game]
    game(id: ID!): Game
    authors: [Author]
    author(id: ID!): Author
}

type Mutation{
    deletegame(id :ID!): [Game]
}

`