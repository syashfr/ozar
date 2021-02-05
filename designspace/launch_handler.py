from az.cli import az
from avionix import ChartBuilder, ChartDependency, ChartInfo

def connect_aks():
     az("aks get-credentials --resource-group ozar-d-rg --name ozar-aks-d")

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
                        "stable",
                    )
                ],
            ),
            [],
        )

    builder.install_chart({"dependency-update": None, "namespace": namespace})