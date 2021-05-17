import { GetStaticProps, GetStaticPaths, NextPage } from 'next'
import Head from 'next/head'
import Link from 'next/link'

import {
  Container,
  Typography,
  Card,
  CardContent,
} from '@material-ui/core'

import { Project } from '../../../src/global.types'
import { getProject, getProjects } from '../../../src/api/projects'

interface StaticProps {
  project: Project
}

type QueryParams = {
  id: string
}

export const getStaticPaths: GetStaticPaths = async () => {
  const projects = await getProjects()

  return {
    paths: projects?.map(({ id }) => `/projects/${id}`) ?? [],
    fallback: true,
  }
}

export const getStaticProps: GetStaticProps<StaticProps, QueryParams> = async ({ params }) => {
  const project = await getProject(params.id)
  return { props: { project } }
} 

const ProjectPage: NextPage<StaticProps> = ({ project }) => {
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
                        language_code: language.language_code,
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
        </Container>
      </main>
    </div>
  )
}

export default ProjectPage