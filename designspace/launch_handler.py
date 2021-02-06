from avionix import ChartBuilder, ChartDependency, ChartInfo

def launch_kicad(release_name, namespace):
    builder = ChartBuilder(
            ChartInfo(
                api_version="v2",
                name=release_name,
                version="0.1.0",
                app_version="1.0.0",
                dependencies=[
                    ChartDependency(
                        "kicad",
                        "0.1.0",
                        "https://syashfr.github.io/kicad/",
                        "kicad-stable",
                    )
                ],
            ),
            [],
        )

    builder.install_chart({"dependency-update": None, "namespace": namespace})


def launch_freecad(release_name, namespace):
    builder = ChartBuilder(
            ChartInfo(
                api_version="v2",
                name=release_name,
                version="0.1.0",
                app_version="1.0.0",
                dependencies=[
                    ChartDependency(
                        "freecad",
                        "0.1.0",
                        "https://syashfr.github.io/freecad/",
                        "freecad-stable",
                    )
                ],
            ),
            [],
        )

    builder.install_chart({"dependency-update": None, "namespace": namespace})

        