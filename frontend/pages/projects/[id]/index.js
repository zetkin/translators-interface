import Head from 'next/head'
import Link from 'next/link'

import Container from '@material-ui/core/Container'
import { Typography, Box, Card, CardContent, Chip } from '@material-ui/core'

import { getProject, getProjects } from '../../../src/api/projects'

export async function getStaticPaths() {
  const projects = await getProjects()

  return {
    paths: projects?.map(({ id }) => `/projects/${id}`) ?? [],
    fallback: true,
  }
}

export async function getStaticProps({ params }) {
  const project = await getProject(params.id)
  return { props: { project } }
}

export default function ProjectPage({ project }) {
  console.log(project)
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
        {/* Projects */}
        {project.languages.map((language) => {
          return (
            <Card key={language.id}>
              <CardContent>
                <Typography gutterBottom variant="h6" component="h4">
                  <Link
                    href={{
                      pathname: '/projects/[id]/[language_code]',
                      query: {
                        id: project.id,
                        language_code: project.language_code,
                      },
                    }}
                  >
                    {language.name}
                  </Link>
                </Typography>
              </CardContent>
            </Card>
          )
        })}
      </main>
    </div>
  )
}
