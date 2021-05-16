import Head from 'next/head'
import Link from 'next/link'

import Container from '@material-ui/core/Container'
import { Typography, Box, Card, CardContent, Chip } from '@material-ui/core'

import { useQuery } from 'react-query'

import { getProject } from '../../../api/projects'

// Index Page - List of projects

export async function getStaticProps(props) {
  console.log(props)
  // Fetch projects
  const projects = await getProject()

  return { props: { projects } }
}

export default function ProjectPage(props) {
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

      <main></main>
    </div>
  )
}
