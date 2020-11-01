
# Toplevel Parser 
parser = argparse.ArgumentParser(
    prog='pake',
    description='peterino\'s highly extensible make-like generic task runner'
)

parser.add_argument(
    'targets', metavar='N', type=int, nargs='*',
    default=['ALL_PAKE_TARGETS'], help="List of targets for "
)

parser.add_argument(
    '--list-jobs', 
    action='store_true', 
    help='Pake, peterino\'s highly extensible make-like generic runner'
)

def main():
    args = parser.parse_args()
