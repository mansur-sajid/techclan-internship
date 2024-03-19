import { ApolloServer } from '@apollo/server';
import { startStandaloneServer } from '@apollo/server/standalone';
import {typeDefs} from './schema.js'
import {games, authors, reviews} from './_db.js';

const resolvers = {
    Query: {
        games() {
            return games
        },
        reviews() {
            return reviews
        },
        authors() {return authors},
        author(_, args){
            return authors.find((author)=> author.id === args.id)
        },
        game(_, args){
            return games.find((game)=> game.id === args.id)
        },
        review(parent, args, context) {
            return reviews.find((review)=> review.id === args.id)
        }
    },
    Review: {
        authors(parent){
            return authors.filter((author)=> author.id === parent.author_id)
        },
        game(parent){
            return games.find((game)=> game.id === parent.game_id)
        }
    },
    Game: {
        reviews(parent){
            return reviews.filter((review)=> review.game_id === parent.id)
        }
    },
    Mutation: {
        deletegame(parent, args){
            const index = games.findIndex((game)=> game.id === args.id)
            if (index>=0){
                games.splice(index, 1)[0]
            }
            return games
        }
    }

}
const server = new ApolloServer({
    typeDefs,
    resolvers
})

const {url} = await startStandaloneServer(server, {
    listen: {port: 4000}
})

console.log("Server ready at port 4000")