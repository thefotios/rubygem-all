## 
#  Bash script for creating rpm from Gemfile
#
#  Author: Fotios Lindiakos (fotios at redhat.com)
#
#  Process derived from: http://yo61.com/building-rpms-from-ruby-gems.html
##

function makerpm() {
  GEMNAME=$@;
  RPMDIR="$HOME/rpmbuild"
  SPECNAME="$RPMDIR/SPECS/rubygem-$GEMNAME.spec";

  # Create the required directories
  mkdir -p $RPMDIR/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

  # Save the current directory and move
  pushd "$RPMDIR/SOURCES"

  # Get the gemfile
  gem fetch $GEMNAME;

  # Generate base specfile
  gem2rpm "$GEMNAME"* > $SPECNAME;

  # Edit the spec.
  # Inside vim run this before quitting to make sure build succeeds: 
  #     rpmbuild -ba %   
  vim $SPECNAME;

  # Run a final build just to make sure it works
  rpmbuild -ba $SPECNAME

  # Add and commit back to the git repo
  git add "$RPMDIR"/**/*"$GEMNAME"* "$RPMDIR"/**/*/*"$GEMNAME"*
  git commit -am "Added $GEMNAME";

  # Go back to the directory
  popd
}

makerpm $@
