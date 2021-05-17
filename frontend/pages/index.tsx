import { GetStaticProps, NextPage } from 'next'
import Head from 'next/head'
import Link from 'next/link'

import { Container, Typography, Box, Card, CardContent, Chip } from '@material-ui/core'

import { Project } from '../src/global.types'
import { getProjects } from '../src/api/projects'

/**
 * Index Page - List Projects
 */

interface StaticProps {projects: Project[]}

export const getStaticProps: GetStaticProps<StaticProps> = async ()=> {
  const projects = await getProjects()
  return { props: { projects } }
}

const Home: NextPage<StaticProps> = ({ projects }) => {
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

          {/* Projects */}
          {projects.map((project) => {
            return (
              <Card key={project.id}>
                <CardContent>
                  <Typography
                    gutterBottom
                    variant="h6"
                    component="h4"
                  >
                    <Link
                      href={{
                        pathname: '/projects/[id]',
                        query: { id: project.id },
                      }}
                    >
                      {project.name}
                    </Link>
                  </Typography>

                  <Typography gutterBottom component="p">
                    <a
                      href={`https://www.github.com/${project.repository_name}`}
                    >
                      {project.repository_name}
                    </a>
                  </Typography>

                  <Box display="flex">
                    {project.languages.map((language) => {
                      return (
                        <Chip
                          label={language.name}
                          style={{ marginRight: 5 }}
                        ></Chip>
                      )
                    })}
                  </Box>
                </CardContent>
              </Card>
            )
          })}
        </Container>
      </main>
    </div>
  )
}

export default Home