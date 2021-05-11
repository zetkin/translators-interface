import Head from 'next/head'

import Container from '@material-ui/core/Container'
import { Typography, Box } from '@material-ui/core'

// Index Page - List of projects

export default function Home() {
  return (
    <div>
      <Head>
        <title>Zetkin Translators Interface</title>
        <meta
          name="description"
          content="Contribute to the localisation of Zetkin's software"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <Container>
          <Box textAlign="center">
            <Typography variant="h2">Projects</Typography>
          </Box>
        </Container>
      </main>
    </div>
  )
}
