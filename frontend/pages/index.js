import Head from 'next/head'

import Container from '@material-ui/core/Container'

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
          <h1>Zetkin Translators Interface</h1>
        </Container>
      </main>
    </div>
  )
}
